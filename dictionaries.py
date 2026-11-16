me = {
  "Name": "Given Mhlongo",
  "Dream": "Software Engineer",
  "University": "UP",
  "Year": 2026
}

#Add a value
me["Sport"] = "Soccer"
me["projects"] = 5

#Change a value
me["Year"] = 2027


for key, value in me.items():
  print(key, ":", value)
