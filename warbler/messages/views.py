from flask import g, redirect, render_template, flash, Blueprint, abort
from warbler.database import db
from warbler.messages.models import Message
from warbler.messages.forms import MessageForm

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)

##############################################################################
# Messages routes:

@messages_blueprint.route('/new', methods=["GET", "POST"])
def add_message():
    """Add a message:

    Show form if GET. If valid, update message and redirect to user page.
    """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    form = MessageForm()

    if form.validate_on_submit():
        msg = Message(text=form.text.data)
        g.user.messages.append(msg)
        db.session.commit()

        return redirect(f"/users/{g.user.id}")

    return render_template('create.html', form=form)


@messages_blueprint.get('/<int:message_id>')
def show_message(message_id):
    """Show a message."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    msg = Message.query.get_or_404(message_id)
    return render_template('show-msg.html', message=msg)

@messages_blueprint.post('/<int:message_id>/like')
def toggle_like(message_id):
    """Toggle a liked message for the currently-logged-in user.

    Redirect to homepage on success.
    """

    form = g.csrf_form

    if not form.validate_on_submit() or not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    liked_message = Message.query.get_or_404(message_id)
    if liked_message.user_id == g.user.id:
        return abort(403)

    if liked_message in g.user.liked_messages:
        g.user.liked_messages.remove(liked_message)
    else:
        g.user.liked_messages.append(liked_message)

    db.session.commit()

    return redirect("/")

@messages_blueprint.post('/<int:message_id>/delete')
def delete_message(message_id):
    """Delete a message.

    Check that this message was written by the current user.
    Redirect to user page on success.
    """

    form = g.csrf_form

    if not form.validate_on_submit() or not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    msg = Message.query.get_or_404(message_id)
    if msg.user_id != g.user.id:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    db.session.delete(msg)
    db.session.commit()

    return redirect(f"/users/{g.user.id}")
