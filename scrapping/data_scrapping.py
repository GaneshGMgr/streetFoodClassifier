from icrawler.builtin import GoogleImageCrawler, BingImageCrawler
import os

food_classes = ['Momo', 'Chowmein', 'Samosa', 'Pakora', 'Spring Roll']
dataset_dir = 'datasets'
search_engines = ['google', 'bing']
images_per_class = 100

food_queries = {
    'Momo': ['Momo', 'Chicken Momo', 'Buff Momo', 'Vegetable Momo', 'Steamed Momo', 'Fried Momo', 'Momo street food', 'Momo recipe'],
    'Chowmein': ['Chowmein', 'Vegetable Chowmein', 'Chicken Chowmein', 'Street Chowmein', 'Chowmein street food', 'Chowmein recipe'],
    'Samosa': ['Samosa', 'Vegetable Samosa', 'Chicken Samosa', 'Meat Samosa', 'Samosa street food', 'Samosa recipe'],
    'Pakora': ['Pakora', 'Vegetable Pakora', 'Chicken Pakora', 'Onion Pakora', 'Spinach Pakora', 'Pakora street food', 'Pakora recipe'],
    'Spring Roll': ['Spring Roll', 'Vegetable Spring Roll', 'Chicken Spring Roll', 'Shrimp Spring Roll', 'Spring Roll street food', 'Spring Roll recipe']
}


os.makedirs(dataset_dir, exist_ok=True)

for food in food_classes:
    food_folder = os.path.join(dataset_dir, food.lower().replace(' ', '_'))
    os.makedirs(food_folder, exist_ok=True)

    for engine in search_engines:
        crawler = GoogleImageCrawler(storage={'root_dir': food_folder}) if engine == 'google' else BingImageCrawler(storage={'root_dir': food_folder})

        for query in food_queries[food]:
            print(f"Downloading {images_per_class} images of '{food}' using query '{query}' from {engine.capitalize()}...")
            crawler.crawl(keyword=query, max_num=images_per_class)

print("Image collection complete!")
