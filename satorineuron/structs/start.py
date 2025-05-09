from enum import Enum
from typing import Union
import threading
from queue import Queue
from reactivex.subject import BehaviorSubject
from satorilib.concepts.structs import StreamId, Stream
from satorilib.wallet import RavencoinWallet, EvrmoreWallet
# from satorilib.ipfs import Ipfs
from satorilib.server import SatoriServerClient
from satorilib.pubsub import SatoriPubSubConn
from satorilib.asynchronous import AsyncThread


class RunMode(Enum):
    normal = 1
    worker = 2
    wallet = 3

    @classmethod
    def choose(cls, runMode):
        # Convert runMode to lowercase if it's a string
        if isinstance(runMode, str):
            runMode = runMode.lower()
        # Define a mapping of possible inputs to Enum values
        mapping = {
            1: cls.normal,
            '1': cls.normal,
            '': cls.normal,
            None: cls.normal,
            'none': cls.normal,
            'normal': cls.normal,
            2: cls.worker,
            '2': cls.worker,
            'worker': cls.worker,
            3: cls.wallet,
            '3': cls.wallet,
            'wallet': cls.wallet,
        }
        # Return the corresponding Enum value
        return mapping.get(runMode, cls.normal)


class StartupDagStruct(object):
    ''' a DAG of startup tasks. '''

    def __init__(
        self,
        env: str = None,
        runMode: RunMode = False,
        urlServer: str = None,
        urlMundo: str = None,
        urlPubsubs: list[str] = None,
        *args
    ):
        self.env = env
        self.runMode = None
        self.workingUpdates: Queue = None
        self.chatUpdates: Queue = None
        self.connectionsStatusQueue: Queue = None
        self.latestConnectionStatus: dict = None
        self.env: str = None
        self.urlServer: str = None
        self.urlMundo: str = None
        self.urlPubsubs: [str] = None
        self.paused: bool = None
        self.pauseThread: Union[threading.Thread, None] = None
        self._ravencoinWallet: RavencoinWallet = None
        self._evrmoreWallet: EvrmoreWallet = None
        self._ravencoinVault: Union[RavencoinWallet, None] = None
        self._evrmoreVault: Union[EvrmoreWallet, None] = None
        self.details: dict = None
        self.key: str = None
        self.oracleKey: str = None
        self.idKey: str = None
        self.subscriptionKeys: str = None
        self.publicationKeys: str = None
        # self.ipfs: Ipfs = None
        self.signedStreamIds: list['SignedStreamId'] = None
        self.relayValidation: 'ValidateRelayStream' = None
        self.server: SatoriServerClient = None
        self.electrumx: Electrumx = None
        self.sub: SatoriPubSubConn = None
        self.pubs: list[SatoriPubSubConn] = []
        self.relay: 'RawStreamRelayEngine' = None
        self.engine: 'satoriengine.Engine' = None
        self.publications: list[Stream] = None
        self.subscriptions: list[Stream] = None
        self.asyncThread: AsyncThread = None
        self.udpQueue: Queue  # TODO: remove
        self.stakeStatus: bool = False

    def cacheOf(self, streamId: StreamId):
        ''' returns the reference to the cache of a stream '''

    @property
    def walletMode(self) -> bool:
        ''' get wallet '''

    @property
    def network(self) -> str:
        ''' get wallet '''

    @property
    def vault(self) -> Union[EvrmoreWallet, RavencoinWallet]:
        ''' get wallet '''

    @property
    def wallet(self) -> Union[EvrmoreWallet, RavencoinWallet]:
        ''' get wallet '''

    @property
    def ravencoinWallet(self) -> RavencoinWallet:
        ''' get wallet '''

    @property
    def evrmoreWallet(self) -> EvrmoreWallet:
        ''' get wallet '''

    def ravencoinVault(
        self,
        password: Union[str, None] = None,
        create: bool = False,
    ) -> Union[RavencoinWallet, None]:
        ''' get the ravencoin vault '''

    def evrmoreVault(
        self,
        password: Union[str, None] = None,
        create: bool = False,
    ) -> Union[EvrmoreWallet, None]:
        ''' get the ravencoin vault '''

    def start(self):
        ''' start the satori engine. '''

    def createRelayValidation(self):
        ''' creates relay validation engine '''

    def networkIsTest(self, network: str = None) -> bool:
        ''' get the ravencoin vault '''

    def getWallet(self, network: str = None) -> Union[EvrmoreWallet, RavencoinWallet]:
        ''' get wallet '''

    def getVault(
        self,
        password: Union[str, None] = None,
        create: bool = False,
    ) -> Union[EvrmoreWallet, RavencoinWallet]:
        ''' get the ravencoin vault '''

    def checkin(self):
        ''' checks in with the Satori Server '''

    def buildEngine(self):
        ''' start the engine, it will run w/ what it has til ipfs is synced '''

    def subConnect(self):
        ''' establish a pubsub connection. '''

    def pubsConnect(self):
        ''' establish a pubsub connection. '''

    def startRelay(self):
        ''' starts the relay engine '''

    # def downloadDatasets(self):
    #    '''
    #    '''
    #    pass

    def pause(self, timeout: int = 60):
        ''' pause the engine. '''

    def unpause(self):
        ''' pause the engine. '''

    def performStakeCheck(self):
        ''' check the stake status '''
