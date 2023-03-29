import abc
import telegram as tg
import telegram.ext as tg_ext


class BaseMessages(abc.ABC):
    @abc.abstractmethod
    def start(self)-> str:
        raise NotImplemented
    
    @abc.abstractmethod
    def help(self)-> str:
        raise NotImplemented
    
    @abc.abstractmethod
    def echo(self, text: str)-> str:
        raise NotImplemented
    

class RegularUser(BaseMessages):
    def start(self)-> str:
        return 'Привет'
    
    def help(self) -> str:
        return 'Вам нужно приобрести подписку'
    
    def echo(self, text: str) -> str:
        return f'{text}'
            
    

class PremiumUser(RegularUser):
    def start(self)-> str:
        return 'Привет Премиум Юзер'

    def help(self) -> str:
        return 'Вам уже приобрели подписку. Менеджер летит к вам'


def get_messages(user: tg.User) -> BaseMessages:
    if user.is_premium:
        return PremiumUser()
    else:
        return RegularUser()