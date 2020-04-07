package {
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import lesta.api.GameAPI;

	public dynamic class MyIcon extends Sprite
	{
		private var _stageWidth:int;
		private var _stageHeight:int;

		public function MyIcon(stageWidth:int, stageHeight:int)
		{
			this._stageWidth = stageWidth;
			this._stageHeight = stageHeight;
		}

		public static function produceIcon(_gameAPI:GameAPI, bmp:Bitmap, col:int, row:int = 2):MyIcon
		{
			var icon:MyIcon = new MyIcon(_gameAPI.stage.width, _gameAPI.stage.height);
			icon.createIcon(bmp, col);
			icon.mouseChildren = icon.mouseEnabled = false;
			return icon;
		}

		public function createIcon(bmp:Bitmap, col:int):void
		{
			this.addChild(bmp);
			this.x = this.getLeftOffset() + this.getColumnStep() * col;
			this.y = this.getTopOffset();
		}

		public function getLeftOffset():int
		{
			return 10;
		}

		public function getTopOffset():int
		{
			return 350;
		}

		public function getColumnStep():int
		{
			return 75;
		}
	}
}//package 
