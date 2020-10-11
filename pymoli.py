import pandas as pd

file_to_load = "purchase_data.csv"

data = pd.read_csv(file_to_load)

## Purchasing Analysis (Total)

player_total = data['SN'].count()
#print(f'Player Total: {player_total}')


unique_items = data['Item Name'].nunique()
average_purchase_price = round(data['Price'].mean(), 2)
revenue = data["Price"].sum()

summary = pd.DataFrame({"Number of Unique Items":[unique_items], "Average Price":[average_purchase_price], "Total Revenue": [revenue]})
#print(summary)


## Gender Demographics

# Percentage and Count of Male Players

male_players = data.groupby('Gender')['SN'].count()['Male']
male_percentage = male_players/player_total * 100

female_players = data.groupby('Gender')['SN'].count()['Female']
female_percentage = female_players/player_total * 100

OtherNonDisclosed = data.groupby('Gender')['SN'].count()['Other / Non-Disclosed']
OtherNonDisclosed_percentage = OtherNonDisclosed/player_total * 100
genderSummary = pd.DataFrame({"Male":[male_players, male_percentage], "Female":[female_players, female_percentage], "Other / Non-Disclosed": [OtherNonDisclosed, OtherNonDisclosed_percentage]})
genderSummary.index = ["Gender Count", "Gender Percentage"]
print(genderSummary)





## Purchasing Analysis (Gender)

# Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender

genders = data.groupby("Gender")

purchase_count = genders["Purchase ID"].count()
gender_average_purchase_price = genders["Price"].mean()
average_purchase_total = genders["Price"].sum()

gender_count = genders.nunique()["SN"]

average_purchase_per_person = average_purchase_total/player_total

genderAnalysisSummary = pd.DataFrame({"Purchase Count":purchase_count, "Average Purchase Price":average_purchase_price, "Average Purchase Value":average_purchase_total, "Avg Purchase Total per Person":average_purchase_per_person})
print(genderAnalysisSummary)




## Age Demographics

# Establish bins for ages

age_bin = [0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99]
age_bin_names = ['<10', '10-14', '15-19','10-24', '25-29', '30-34', '35-39']
# Categorize the existing players using the age bins. Hint: use pd.cut()


