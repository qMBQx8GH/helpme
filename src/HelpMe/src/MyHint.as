package {
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import lesta.api.GameAPI;

	public dynamic class MyHint extends Sprite
	{
		private var _stageWidth:int;
		private var _stageHeight:int;
		private var _rowsOffset:Array;
		private var _width:int;
		private var _iconSize:int;
		private var _padding:int;

		public function MyHint(stageWidth:int, stageHeight:int)
		{
			this._stageWidth = stageWidth;
			this._stageHeight = stageHeight;
			this._rowsOffset = [180, 260, 370];
			this._width = 495;
			this._iconSize = 68;
			this._padding = 10;
		}

		public static function produceHint(_gameAPI:GameAPI, col:int, row:int):MyHint
		{
			var hint:MyHint = new MyHint(_gameAPI.stage.width, _gameAPI.stage.height);
			hint.createHint(col, row);
			return hint;
		}

		public function createHint(col:int, row:int):void
		{
			this.graphics.lineStyle(1, 0xfbc62c);
			var width:int = 68;
			var left:int = this._padding + (this._iconSize + this.getColumnSpace()) * col;
			this.graphics.drawRoundRect(
				left,
				this._rowsOffset[row],
				this._iconSize, this._iconSize, 6
			);
			this.graphics.moveTo(
				left + this._iconSize,
				this._rowsOffset[row] + 3
			);
			this.graphics.lineTo(
				left + this._iconSize,
				this._rowsOffset[row] + this._iconSize - 3
			);
		}

		public function getColumnSpace():int
		{
			return (this._width - this._padding - this._padding - this._iconSize * 6) / 5;
		}
	}
}//package 
