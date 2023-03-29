import abc
import telegram as tg
import telegram.ext as tg_ext


class BaseHandler(abc.ABC):
    @abc.abstractmethod
    async def __call__(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE)-> None:
        raise NotImplemented

class StartHandler(BaseHandler):
    async def __call__(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        user = update.effective_user
        await update.message.replay_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=tg_ext.ForceReply(selective=True),
    )

class HelpHandler(BaseHandler):
    async def __call__(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.replay_text('Help!')

class EchoHandler(BaseHandler):
    async def __call__(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.replay_text(update.message.text)




def setup_handlers(application: tg_ext.Application) -> None:
    application.add_handler(tg_ext.CommandHandler('start', StartHandler()))
    application.add_handler(tg_ext.CommandHandler('help', HelpHandler()))

    application.add_handler(
        tg_ext.MessageHandler(tg_ext.filters.TEXT & ~tg_ext.filters.COMMAND, EchoHandler())
    )