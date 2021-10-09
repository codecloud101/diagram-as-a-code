from diagrams import Diagram
from diagrams.alibabacloud.web import Domain
from diagrams.alibabacloud.compute import ECS
from diagrams.alibabacloud.database import ApsaradbRedis
from diagrams.alibabacloud.database import HybriddbForMysql
from diagrams.alibabacloud.network import Cdn

with Diagram("Wordpress ECS", show=False):
     Domain("codecloud101.com") >> Cdn("CDN") >> ECS("WordPress") >> ApsaradbRedis("REDIS") >> HybriddbForMysql("MySQL")