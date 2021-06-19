# Create a virtual env
python -m venv azure-devops

# Source virtual env
source ~/-azure-devops/bin/activate

# Run make file 
make all

# Run the webapp
az webapp up -n flask-ml-service-2

# Display latest logs of the webapp
az webapp log tail --name flask-ml-service-2

# Run prediction
./make_prediction_axure_app.sh