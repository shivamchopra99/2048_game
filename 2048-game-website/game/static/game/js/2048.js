var Game = (function() {
    var mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
    var score = 0;
    var show2048dialog = 0;
    var prevmax=4;
    var p;
    // function to change state of mat;
    // and set show2048dialog variable if required
    function moveLeft(){
        var i=0;
        while(i<=3)
        {
            var start=0,end=3,start2=0;
            while(start<end)
            {
                if(mat[i][start]===0)
                {
                    var k=start;
                    while(k<end)
                    {
                        mat[i][k]=mat[i][k+1];
                        k=k+1;
                    }
                    mat[i][end]=0;
                    k=start;
                    while(k<=end)
                    {
                        if(mat[i][k]!==0)
                            break;
                        k=k+1;
                    }
                    if(k===end+1)
                        {start=end;}
                        else{
                            start=start2;
                        }

                
                }
                else if(mat[i][start]===mat[i][start+1])
                {if(mat[i][start]!=0)
                    {mat[i][start]=2*mat[i][start];
                        score=score+mat[i][start];
                    mat[i][start+1]=0;
                    start=start+1;
                    start2=start;
                }}
                    else{
                        start=start+1;
                    }
                
            }
            i=i+1;
        }}
    
    
    function moveRight() {
        var i=0;
        while(i<4)
        {
            var j=0,k=3;
            while(j<=k)
            {
                var temp=mat[i][j];
                mat[i][j]=mat[i][k];
                mat[i][k]=temp;
                j=j+1;
                k=k-1;
            }
            i=i+1;
        }
        moveLeft();
        i=0;
        while(i<4)
        {
            var j=0,k=3;
            while(j<=k)
            {
                var temp=mat[i][j];
                mat[i][j]=mat[i][k];
                mat[i][k]=temp;
                j=j+1;
                k=k-1;
            }
            i=i+1;
        }
    }
    function moveTop() {
        var i=0,j=0;
        while(i<=3)
        {var k=j;
            while(j<=3)
            {
                var temp=mat[i][j];
                mat[i][j]=mat[j][i];
                mat[j][i]=temp;
                j=j+1;
            }
            j=k+1;
            i=i+1;
        }
        moveLeft();
        i=0,j=0;
        while(i<=3)
        {var k=j;
            while(j<=3)
            {
                var temp=mat[i][j];
                mat[i][j]=mat[j][i];
                mat[j][i]=temp;
                j=j+1;
            }
            j=k+1;
            i=i+1;
        }

    }
    function moveDown() {
        var i=0,j=0;
        while(i<=3)
        {var k=j;
            while(j<=3)
            {
                var temp=mat[i][j];
                mat[i][j]=mat[j][i];
                mat[j][i]=temp;
                j=j+1;
            }
            j=k+1;
            i=i+1;
        }
        moveRight();
        i=0,j=0;
        while(i<=3)
        {var k=j;
            while(j<=3)
            {
                var temp=mat[i][j];
                mat[i][j]=mat[j][i];
                mat[j][i]=temp;
                j=j+1;
            }
            j=k+1;
            i=i+1;
        }

    }


    // reflect state of mat
    function redraw() {

    var k=document.getElementsByClassName("tile");
    var i=0;
    while(i<k.length)
    {
        k[i].classList.remove("tile_0","tile_2","tile_4","tile_8","tile_16","tile_32","tile_64","tile_128","tile_256","tile_512","tile_1024","tile_2048","tile_4096");
        i=i+1;
    }
    i=0;
    var j=0,m=0;
    while(i<k.length)
    {document.getElementById("score").innerHTML=score;
       k[i].innerHTML=mat[j][m];
       var t="tile_"+mat[j][m];
       if(mat[j][m]>=4096)
        t="tile_4096";
       k[i].classList.add(t);
       if(mat[j][m]===0)
        k[i].innerHTML="";
    
       i=i+1;
       m=m+1;
       if(m===4)
       {
        m=0;
        j=j+1;
       }

    }
    var max=0;
    for(var i=0;i<4;i++)
        for(var j=0;j<4;j++)
            if(mat[i][j]>max)
                max=mat[i][j];
    var ele="tile_"+max;
    var x=document.getElementsByClassName(ele);
    for(var i=0;i<x.length;i++)
        {if(max>prevmax){
            $(x[i]).animate({
           opacity:'0.5',
        },'slow')
        $(x[i]).animate({
            opacity:'1',
        },'slow')
      }}
        prevmax=max;



    }

    // randomw number between 2 and 4
    function getRandomValue() {
        var k=Math.floor((Math.random())*2+1);
        if(k===1)
            return 2;
        if(k===2)
        return 4;
    }

    // returns x.y of a random empty cell
    function getRandomEmptyCell() {
        while(1){
var k=Math.floor((Math.random())*16);
//console.log(k);
var p=Math.floor(k/4);
var t=Math.floor(k%4);
//console.log(p);
//console.log(t);
if(mat[p][t]===0)
{
    s={
        x:p,
        y:t
    }

break;
}}
return s;}
  function fillOneRandomEmptyCell() {
        var coord = getRandomEmptyCell();
        var value = getRandomValue();
        mat[coord.x][coord.y] = value;
        //console.log(mat);
    }

    // checks if gameover
    function isGameOver() {
        var x=0,y=0;
        while(x<4)
        {y=0;
            while(y<4)
            {
                if(mat[x][y]==0)
                    break;
                y=y+1;
            }
            if(mat[x][y]==0)
                break;
            x=x+1;
        }
        for(var u=0;u<4;u++)
        {
            for(var e=0;e<4;e++)
            {
                if(e!=3&&(mat[u][e]==mat[u][e+1]))
                    return false;
                if(u!=3&&(mat[u][e]==mat[u+1][e]))
                    return false;

            }
        }
        if(x===4)
            {if(y===4)
            return true;}
        return false;
    }

    // show Dialog for GameOver()
    function showGameOverDialog() {
        if(isGameOver()===true)
        {
            document.getElementById("lose").style.display="block";
            window.removeEventListener('keydown',move);
        }
    }

    // show dialog for 2048
    function show2048Dialog() {
       var i=0,j=0;
       while(i<4)
       {j=0;
        while(j<4)
        {
            if(mat[i][j]===2048)
                break;
            j=j+1;
        }
        if(mat[i][j]===2048)
            break;
        i=i+1;
       }
       if(i===4)
       {
        if(j===4)
            return;
       }
          else{
          document.getElementById("win").style.display="block";
          show2048dialog=1;}

            


    }
    function undoLocal(vat,prev)
    {var myarr=JSON.parse(localStorage.getItem('myarr'));
    if(myarr==undefined)
       myarr=[];
   var myscore=JSON.parse(localStorage.getItem('myscore'));
   if(myscore==undefined)
    myscore=[];
       var myarr1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
       for(var i=0;i<4;i++)
        for(var j=0;j<4;j++)
            myarr1[i][j]=vat[i][j];
        myarr.push(myarr1);
        var prev1=prev;
        myscore.push(prev1);
        localStorage.setItem('myarr', JSON.stringify(myarr));
        localStorage.setItem('myscore', JSON.stringify(myscore));

    }


    function move(e) {
        //depending upon keypress you call the respective function
        var vat=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
        for(var b=0;b<4;b++)
            for(var d=0;d<4;d++)
                vat[b][d]=mat[b][d];
            var prev=score;
        e.preventDefault();
        if(e.which===37)
            moveLeft();
        else if(e.which===38)
            moveTop();
        else if(e.which===39)
            moveRight();
        else if(e.which===40)
            moveDown();
        else{
            return;
        }
        if (isGameOver()) {
            showGameOverDialog();
        }
        var c=0;
        for(var l=0;l<4;l++)
        {
            for(var t=0;t<4;t++)
                if(mat[l][t]!=vat[l][t])
                {
                    c=1;
                    break;
                }
        }

        if(c==1){ 
            undoLocal(vat,prev);
       fillOneRandomEmptyCell();}
        redraw();
        if (isGameOver()) {
            showGameOverDialog();
        }
        if (show2048dialog === 0) {
            show2048Dialog();
            //show2048dialog =1;
        }
    }
    function retrieve()
    {//localStorage.clear();
        var retrieveObject=JSON.parse(localStorage.getItem('mat'));
        var retrieveScore=JSON.parse(localStorage.getItem('score'));
        var player_name=JSON.parse(localStorage.getItem('name'));
        if(retrieveObject==undefined)
            reset();
        else
            mat=retrieveObject;
            reset();
        // else
        //   score=retrieveScore;

        if(player_name==undefined)
            reset();
        else if(player_name!==p)
            {console.log('player',player_name,'current',p);
            reset();
        }
        redraw();

    }
    function undo()
    {
        var myarr=JSON.parse(localStorage.getItem('myarr'));
        if(myarr.length>0){
            var myarr2=myarr.pop();
            for(var i=0;i<4;i++)
                for(var j=0;j<4;j++)
                    mat[i][j]=myarr2[i][j];
                var myscore=JSON.parse(localStorage.getItem('myscore'));
                score=myscore.pop();
                redraw();
            localStorage.removeItem('myarr');
            localStorage.removeItem('myscore');
            localStorage.setItem('myarr',JSON.stringify(myarr));
            localStorage.setItem('myscore',JSON.stringify(myscore));
                        document.getElementById("lose").style.display="none";
            window.addEventListener('keydown',move);
        }
        else
            alert("Sorry !! No more steps to undo");

    }
    function reset(e) {
        if (e !== undefined) {
            e.preventDefault();
        }
        //console.log("hii");
        mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
        var k=document.getElementsByClassName("tile");
        //console.log(localStorage.getItem('mat'));
        //mat=JSON.parse(localStorage.getItem('mat'));
        score = 0;
        document.getElementsByClassName('colorch')[0].innerHTML='Score';
        fillOneRandomEmptyCell();
        fillOneRandomEmptyCell();
        //console.log(mat);
        redraw();
        document.getElementById("lose").style.display="none";
        //document.getElementById("win").style.display="none";
        window.removeEventListener('keydown', move);
        window.addEventListener('keydown',move);
        localStorage.removeItem('myarr');
    }
    function doit(){
        document.getElementById("win").style.display="none";
    }
    function local()
    {
        localStorage.setItem('mat', JSON.stringify(mat));
        localStorage.setItem('score', JSON.stringify(score));
        localStorage.setItem('name',JSON.stringify(p));

    }
    function init(z) {
        //console.log("hiii");
        p=z;
        retrieve();
        
        //console.log("hii");

        // add reset method on click actions of all the reset elements'
        window.addEventListener('keydown',move);
        document.getElementById("res").addEventListener('click', reset);
        document.getElementById("yes").addEventListener('click', doit);
        document.getElementById("reset1").addEventListener('click', reset);
        document.getElementById('undo1').addEventListener('click',undo);
        window.addEventListener('unload',local);
    }
    return {
        init : init
    };
})();