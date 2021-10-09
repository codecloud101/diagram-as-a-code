from diagrams import Diagram
from diagrams.alibabacloud.web import Domain
from diagrams.alibabacloud.compute import SAS

with Diagram("Wordpress SAS", show=False):
     Domain("codecloud101.com") >> SAS("WordPress")
