# include <Siv3D.hpp> // OpenSiv3D v0.6.4

void Main()
{
	FontAsset::Register(U"result", 20);
	FontAsset::Register(U"title", 60);
	const URL host = U"http://suzakutakumi.mydns.jp:5000";
	const URL endpoint = U"/analyze";
	const HashTable<String, String> headers = { {U"Content-Type",U"text/plain"} };
	const FilePath result = U"result.txt";

	TextEditState state;

	String text = U"",origin;

	Scene::SetBackground(Palette::White);

	while (System::Update())
	{
		SimpleGUI::TextBoxAt(state, Scene::Size()*Vec2(0.5,0.4), Scene::Width() * 0.8);
		if (KeyEnter.down() or SimpleGUI::ButtonAt(U"Enter",Scene::Size() * Vec2(0.5, 0.5))) {
			std::string data=state.text.narrow();
			if (HTTPResponse res=SimpleHTTP::Post(host + endpoint, headers, data.data(), data.size(), result)) {
				if (res.isOK()) {
					origin = state.text;
					text = TextReader{result}.readAll();
				}
			}
		}

		FontAsset(U"title")(U"Analyze Corner").drawAt(Vec2(Scene::Width()/2.0,Scene::Height()*0.1), Palette::Skyblue);

		const Vec2 base(Scene::Width() * 0.1, Scene::Height()* 0.6);
		Vec2 pen = base;
		int n=origin.indexOf(U"_");
		int i = 0;
		for (const auto& glyph : FontAsset(U"result").getGlyphs(origin.substr(0,n)+text+origin.substr(n+1)))
		{
			ColorF color = Palette::Black;
			if (n<=i&&i<=n+text.length())
			{
				color = Palette::Orange;
			}	

			// 文字のテクスチャをペンの位置に文字ごとのオフセットを加算して描画
			// FontMethod がビットマップ方式の場合に限り、Math::Round() で整数座標にすると品質が向上
			glyph.texture.draw(Math::Round(pen + glyph.getOffset()), color);

			// ペンの X 座標を文字の幅の分進める
			pen.x += glyph.xAdvance;
			i++;
		}
	}
}
