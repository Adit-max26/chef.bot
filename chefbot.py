# =========================


def greet():
    print("🍳 Halo! Aku ChefBot, asisten memasakmu.")
    print("Aku bisa membantu resep, tips memasak, dan ide menu.")
    print("Ketik 'keluar' untuk mengakhiri percakapan.\n")


def recommend_recipe(ingredients):
    if "telur" in ingredients and "mie" in ingredients:
        return (
            "🍜 Rekomendasi: Mie Goreng Telur\n"
            "Langkah singkat:\n"
            "1. Rebus mie hingga setengah matang\n"
            "2. Tumis bumbu mie\n"
            "3. Masukkan telur dan orak-arik\n"
            "4. Masukkan mie, aduk rata\n"
        )
    elif "nasi" in ingredients and "telur" in ingredients:
        return (
            "🍚 Rekomendasi: Nasi Goreng Telur\n"
            "Langkah singkat:\n"
            "1. Tumis bawang\n"
            "2. Masukkan telur\n"
            "3. Masukkan nasi\n"
            "4. Bumbui dan aduk rata\n"
        )
    else:
        return "😅 Maaf, aku belum punya resep dari bahan tersebut."


def cooking_tips():
    tips = [
        "🔥 Panaskan wajan sebelum memasak agar tidak lengket",
        "🧂 Bumbui sedikit demi sedikit",
        "⏱ Jangan memasak dengan api terlalu besar",
        "🔪 Gunakan pisau tajam agar potongan rapi"
    ]
    return "\n".join(tips)


def chatbot():
    greet()

    while True:
        user_input = input("Kamu: ").lower()

        if user_input == "keluar":
            print("👋 Terima kasih! Selamat memasak!")
            break

        elif "resep" in user_input or "masak" in user_input:
            bahan = input("🧺 Sebutkan bahan yang kamu punya (pisahkan dengan koma): ")
            ingredients = bahan.lower().split(",")
            print(recommend_recipe(ingredients))

        elif "tips" in user_input:
            print("📌 Tips Memasak:")
            print(cooking_tips())

        else:
            print("🤔 Aku bisa bantu resep atau tips memasak. Coba ketik 'resep' atau 'tips'.")


# Menjalankan chatbot
if __name__ == "__main__":
    chatbot()
