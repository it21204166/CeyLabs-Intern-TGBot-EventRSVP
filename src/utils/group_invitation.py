# src/utils/group_invitation.py
import logging

async def invite_user_to_group(chat_id: int, group_invite_link: str, context):
    try:
        if group_invite_link:
            await context.bot.send_message(chat_id, f"Please join the event group using this link: {group_invite_link}")
        else:
            logging.warning("No group invite link found")
    except Exception as e:
        logging.error(f"Error adding user to group: {e}")
