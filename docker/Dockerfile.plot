ARG sourceimage=HuangTraderorg/HuangTrader
ARG sourcetag=develop
FROM ${sourceimage}:${sourcetag}

# Install dependencies
COPY requirements-plot.txt /HuangTrader/

RUN pip install -r requirements-plot.txt --user --no-cache-dir
