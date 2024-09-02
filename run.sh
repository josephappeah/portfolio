cd ./trading-service/requirements
pip install -r requirements.txt
cd ../trader
export PYTHONPATH="$PYTHONPATH:/home/ec2-user/portfolio/trading-service/"
nohup python3.10 Trader.py &

import sys
sys.path.append("~/portfolio/trading-service/")

cd ./ui
npm install
nohup npm run start > ./ui-logs.txt &