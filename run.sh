# SERVER
cd ./trading-service/requirements
pip3.10 install -r requirements.txt
cd ../trader
export PYTHONPATH="$PYTHONPATH:/home/ec2-user/portfolio/trading-service/"
nohup python3.10 Trader.py &

# UI
nvm install 16.0.0
cd ./ui/projects
npm install
nohup npm run start > ./ui-logs.txt &