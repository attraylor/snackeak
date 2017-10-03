function f(sObj){
   var val = sObj.value;
   
   switch (val) {
    case "c326":
        document.getElementById('c3').style.display = 'block';
		document.getElementById('c4').style.display = 'none';
		document.getElementById('c34').style.display = 'none';
		document.getElementById('m5').style.display = 'none';
        break;
    case "c453":
        document.getElementById('c3').style.display = 'none';
		document.getElementById('c4').style.display = 'block';
		document.getElementById('c34').style.display = 'none';
		document.getElementById('m5').style.display = 'none';
        break;
	case "c345":
		document.getElementById('c3').style.display = 'none';
		document.getElementById('c4').style.display = 'none';
		document.getElementById('c34').style.display = 'block';
		document.getElementById('m5').style.display = 'none';
        break;
	case "m551":
		document.getElementById('c3').style.display = 'none';
		document.getElementById('c4').style.display = 'none';
		document.getElementById('c34').style.display = 'none';
		document.getElementById('m5').style.display = 'block';
        break;
    }
}



	
	



