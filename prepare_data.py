import json

new: list[dict[str, str]] = []

with open("og.json", "r") as f:
    og = json.load(f)

print(og[0]["tag"])
print(og[0]["questionTitle"])

og_tag: str = input("Enter og tag: ")
new_tag: str = input("Enter new tag: ")
og_title: str = input("Enter og title: ")
new_title: str = input("Enter new title: ")

for obj in og:
    new.append(
        {
            "postID": obj["postID"],
            "questionTitle": obj["questionTitle"].replace(og_title, new_title),
            "tag": obj["tag"].replace(og_tag, new_tag),
        }
    )


with open("new.json", "w") as f:
    json.dump(new, f, indent=4)
