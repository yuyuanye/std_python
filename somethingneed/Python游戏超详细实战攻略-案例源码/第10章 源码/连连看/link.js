function _index(_value){
	for(var v in this){
		if(this[v] == _value){
			return new Number(v)
		}
	}
	return -1;
}

function _remove(_value){
	var _index = this.index(_value);
	this.splice(_index,1);
}

function _insert(_position,_value){
	this.splice(_position,0,_value);
}

Array.prototype.index = _index;
Array.prototype.insert = _insert;
Array.prototype.remove = _remove;

function Point(_x,_y,_value){
	this.x = _x;
	this.y = _y;
	this.value = _value;
	this.directs = null;
	this.changed = 0;
}

function _createDirect(_pre,_target){
	this.directs = new Array();
	var stx = _target.x - this.x;
	var sty = _target.y - this.y;
	if(stx >= 0){
		this.directs.push("right");
		this.directs.push("left");
	}
	else{
		this.directs.push("left");
		this.directs.push("right");
	}
	if(sty >= 0){
		this.directs.insert(1,"up");
		this.directs.push("down");
	}
	else{
		this.directs.insert(1,"down");
		this.directs.push("up");
	}
	if (_pre == null){
		return ;
	}
	var spx = _pre.x - this.x;
	var spy = _pre.y - this.y;
	if (spx == 0){
		if (spy == 1){
			this.directs.remove("up");
		}
		else{
			this.directs.remove("down");
		}
	}
	else{
		if (spx == 1){
			this.directs.remove("right");
		}
		else{
			this.directs.remove("left");
		}
	}
}

function _forward(_pre,_target){
	if(this.directs == null){
		this.createDirect(_pre,_target);
	}
	if(this.directs.length == 0){
		return null;
	}
	var direct = null;
	var tmpDirect = null;
	var x = null;
	var y = null;
	var p = null;
	while(true){
		if(this.directs.length == 0){
			break;
		}
		tmpDirect = this.directs.shift();
		switch(tmpDirect){
			case "up":
				x = this.x;
				y = this.y + 1;
				break;
			case "down":
				x = this.x;
				y = this.y - 1;
				break;
			case "left":
				x = this.x - 1;
				y = this.y;
				break;
			case "right":
				x = this.x + 1;
				y = this.y;
				break;
			default:
				throw new Error("error direct");
				break;
		}
		p = points[x][y];
		if(p.value > 0 && p != _target){
			continue;
		}
		else{
			direct = tmpDirect;
			if(_pre == null){
				this.changed = 1;
			}
			else{
				if((_pre.x - this.x) == 0 && (p.x - this.x) == 0){
					this.changed = 0;
				}
				else{
					if((_pre.y - this.y) == 0 && (p.y - this.y) == 0){
						this.changed = 0;
					}
					else{
						this.changed = 1;
					}
				}
			}
			break;
		}
	}
	return direct;
}

function _equals(_point){
	if (_point == null){
		return false;
	}
	if (this.x == _point.x && this.y == _point.y){
		return true;
	}
	else{
		return false;
	}
}

Point.prototype.createDirect = _createDirect;
Point.prototype.forward = _forward;
Point.prototype.equals = _equals;

var points = new Array();
var valueStack = new Array();

function createPoints(w,h){
	var temp;
	var tempValue;
	pointStack(w,h);
	for(var _x = 0 ; _x < w ; _x++){
		temp = new Array();
		for(var _y = 0 ; _y < h ; _y++){
			if(_x == 0 || _x == (w-1) || _y == 0 || _y == (h-1)){
				tempValue = 9;
			}
			else{
				if(_x == 1 || _x == (w-2) || _y == 1 || _y == (h-2)){
					tempValue = 0;
				}
				else{
					tempValue = valueStack.pop();
				}
			}
			temp[_y] = new Point(_x,_y,tempValue);
		}
		points[_x] = temp;
	}
}

function pointStack(w,h){
	var size = (w*h-(w*4+h*4-16))/2;
	var pointValue;
	for(var i = 0 ; i < size ; i++){
		while(true){
			pointValue = Math.floor(Math.random()*9);
			if(pointValue != 0){
				break;
			}
		}
		valueStack.insert(Math.floor(Math.random()*valueStack.length),pointValue);
		valueStack.insert(Math.floor(Math.random()*valueStack.length),pointValue);
	}
}

function linkPoints(_source,_target){
	var path = new Array();
	var fail = new Object();
	var change = 0;
	var _current = _source;
	var direct = null;
	var _x,_y;
	while(true){
		//alert("current--"+pointStr(_current)+"change:"+change);
		if(_current == _target && change < 4){
			path.push(_target);
			for(var p in path){
				path[p].directs = null;
			}
			return path;
		}
		if(change == 4){
			_current.directs = null;
			fail[(_current.x+"_"+_current.y)] = change;
			_current = path.pop();
			change = change - _current.changed;
			continue;
		}
		if(_current == _source){
			direct = _current.forward(null,_target);
		}
		else{
			direct = _current.forward(path[path.length-1],_target);
		}
		if(direct != null){
			if(direct == "up"){
				_x = _current.x;
				_y = _current.y + 1;
			}
			if(direct == "down"){
				_x = _current.x;
				_y = _current.y - 1;
			}
			if(direct == "left"){
				_x = _current.x - 1;
				_y = _current.y ;
			}
			if(direct == "right"){
				_x = _current.x + 1;
				_y = _current.y;
			}
			if(fail[(_x+"_"+_y)] != null){
				if (change >= fail[(_x+"_"+_y)]){
					continue;
				}
				else{
					delete fail[(_x+"_"+_y)];
				}
			}
			change = change + _current.changed;
			path.push(_current);
			_current = points[_x][_y];
		}
		else{
			if(_current == _source){
				_source.directs = null;
				return false;
			}
			else{
				_current.directs = null;
				fail[(_current.x+"_"+_current.y)] = change;
				_current = path.pop();
				change = change - _current.changed;
			}
		}
	}
}

/*function pointStr(p){
	return " x:"+p.x+" y:"+p.y+" value:"+p.value;
}
*/
