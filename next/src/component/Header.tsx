import React from 'react';
import { Search, Bell } from 'lucide-react';

const Header = () => {
  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-4 py-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <img src="/api/placeholder/120/40" alt="Mercari logo" className="h-10" />
            <div className="relative">
              <input
                type="text"
                placeholder="なにをお探しですか？"
                className="pl-10 pr-4 py-2 border border-gray-300 rounded-md w-64"
              />
              <Search className="absolute left-3 top-2.5 text-gray-400" size={20} />
            </div>
          </div>
          <div className="flex items-center space-x-4">
            <button className="text-gray-600 hover:text-gray-800">ログイン</button>
            <button className="text-gray-600 hover:text-gray-800">会員登録</button>
            <Bell className="text-gray-600" size={20} />
            <button className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600">
              出品
            </button>
          </div>
        </div>
        <nav className="mt-4">
          <ul className="flex space-x-6 text-sm">
            <li className="text-red-500 border-b-2 border-red-500 pb-2">おすすめ</li>
            <li className="text-gray-600 hover:text-gray-800">マイリスト</li>
            <li className="text-gray-600 hover:text-gray-800">ゲーム・おもちゃ・グッズ</li>
            <li className="text-gray-600 hover:text-gray-800">本・雑誌・漫画</li>
            <li className="text-gray-600 hover:text-gray-800">メンズ</li>
            <li className="text-gray-600 hover:text-gray-800">レディース</li>
            <li className="text-gray-600 hover:text-gray-800">ベビー・キッズ</li>
            <li className="text-gray-600 hover:text-gray-800">すべて見る</li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;