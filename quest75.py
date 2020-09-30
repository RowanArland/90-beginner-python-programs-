team_name = ["Liverpool", "United", "Spurs", "Chelsea"]
print("Team Name",team_name)
Manager_name = ["Klopp", "ole", "Pochatino", "Lampard"]
print("Manager Name",Manager_name)
print([{'Team Name': t, 'Manager Name': m}
       for t, m in zip(team_name, Manager_name)])
