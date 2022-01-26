from vkbottle.bot import Blueprint, Message, rules

bp = Blueprint("for admin commands")
bp.labeler.auto_rules = [rules.FromPeerRule(360063282)]


@bp.on.message(command="halt")
async def halt():
    exit(0)
