#wind speed track
data=cd.read_csv("sat.csv")
timestamp=42368.1491555
dt_object=datetime.fromtimestamp(timestamp)
for i in data["time"]:
    dt_object=datetime.fromtimestamp(i)
    print(dt_object)
data["Time_Analysis"]=pd.to_datetime(data["time"],unit="s")
data.wind_speed.isnull().sum()
data=data.dropna(how="any",axis=0)
data.shape
feature_col=["X","Y","time"]
target=["wind_speed"]
X=data[feature_col]
