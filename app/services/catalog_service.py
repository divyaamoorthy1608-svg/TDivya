CATALOG = [
{
"name": "Minimal Desk Lamp",
"category": "Home",
"price": 899,
"source": "Amazon demo link",
"link": "https://www.amazon.in/",
"tags": [
"bedroom",
"study",
"modern",
],
},
{
"name": "Decorative Cushion Set",
"category": "Home",
"price": 699,
"source": "IKEA demo link",
"link": "https://www.ikea.com/in/en/",
"tags": [
"bedroom",
"living",
"simple",
],
},
{
"name": "LED String Lights",
"category": "Home",
"price": 499,
"source": "Flipkart demo link",
"link": "https://www.flipkart.com/",
"tags": [
"party",
"bedroom",
"decoration",
],
},
{
"name": "Simple Party Decoration Kit",
"category": "Party",
"price": 799,
"source": "Amazon demo link",
"link": "https://www.amazon.in/",
"tags": [
"birthday",
"party",
"simple",
],
},
{
"name": "Snack Combo",
"category": "Party",
"price": 1200,
"source": "Swiggy demo link",
"link": "https://www.swiggy.com/",
"tags": [
"birthday",
"food",
"party",
],
},
{
"name": "Cake",
"category": "Party",
"price": 650,
"source": "Zomato demo link",
"link": "https://www.zomato.com/",
"tags": [
"birthday",
"food",
],
},
{
"name": "Stud Earrings",
"category": "Jewelry",
"price": 799,
"source": "Amazon demo link",
"link": "https://www.amazon.in/",
"tags": [
"earrings",
"college",
"simple",
],
},
{
"name": "Artificial Pearl Necklace",
"category": "Jewelry",
"price": 999,
"source": "Flipkart demo link",
"link": "https://www.flipkart.com/",
"tags": [
"necklace",
"function",
"simple",
],
},
{
"name": "Minimal Bracelet",
"category": "Jewelry",
"price": 599,
"source": "Amazon demo link",
"link": "https://www.amazon.in/",
"tags": [
"bracelet",
"college",
"simple",
],
},
]

def get_catalog(planner_type: str) -> list[dict]:
    category = {
        "home": "Home",
        "party": "Party",
        "jewelry": "Jewelry",
    }.get(planner_type.lower())

    return [
        item
        for item in CATALOG
        if item["category"] == category
    ]

