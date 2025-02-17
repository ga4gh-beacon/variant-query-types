BASEDIR=$(dirname $0)
UNITYPATH=$BASEDIR/..
$BASEDIR/beaconYamler.py -i $UNITYPATH/src -t yaml -x json -o $UNITYPATH/json
