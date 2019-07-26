package {
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import lesta.api.GameAPI;

	public dynamic class MyHint extends Sprite
	{
		private var _stageWidth:int;
		private var _stageHeight:int;

		public function MyHint(stageWidth:int, stageHeight:int)
		{
			this._stageWidth = stageWidth;
			this._stageHeight = stageHeight;
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
			var left:int = this.getLeftPadding() + (this.getIconSize() + this.getColumnSpace()) * col;
			this.graphics.drawRoundRect(
				left,
				this.getTopOffset() + this.getRowStep() * row,
				this.getIconSize(), this.getIconSize(), 6
			);
			this.graphics.moveTo(
				left + this.getIconSize(),
				this.getTopOffset() + this.getRowStep() * row + 3
			);
			this.graphics.lineTo(
				left + this.getIconSize(),
				this.getTopOffset() + this.getRowStep() * row + this.getIconSize() - 3
			);
		}

		public function getWidth():int
		{
			if (this._stageWidth < 1400) {
				return 535;
			} else {
				return 500;
			}
		}
		
		public function getIconSize():int
		{
			return 68;
		}

		public function getRightPadding():int
		{
			return 10;
		}

		public function getLeftPadding():int
		{
			return 20;
		}

		public function getColumnSpace():int
		{
			return (this.getWidth() - this.getLeftPadding() - this.getRightPadding() - this.getIconSize() * 6) / 5;
		}

		public function getTopOffset():int
		{
			if (this._stageWidth < 1400) {
				return 213;
			} else {
				return 199;
			}
		}

		public function getRowStep():int
		{
			return 70;
		}
	}
}//package 
