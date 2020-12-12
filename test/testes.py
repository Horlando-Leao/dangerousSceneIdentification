import sys

sys.path.append("src\controllers")

from handilingAuto import handiling_auto

url = "https://cdn-istoe-ssl.akamaized.net/wp-content/uploads/sites/14/2019/01/e7f66c0f0c153eba4cbf868f5eccab26632176e2.jpg"
print(handiling_auto(url))