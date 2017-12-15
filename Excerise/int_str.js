var n = 1233;
var a=[];

var spell=[];
var d = n.toString();
console.log("D:",d);
console.log("D length:",d.length);

for(var i=0;i<=d.length;i++)
{
    //d=n%10;
    a.push(+d.charAt(i));
    
}
console.log("a[]:",a);
console.log("a[] legth:",a.length)

for(var i=0;i<=a.length;i++)
{
   var l=a[i];
   console.log("l:",l);
    if(l=='1'){
        l='one';
        spell.push(l);
    }
    else if(l=='2'){

        l='two'
        spell.push(l);  
    }
    else if(l=='3')
    {
        l='three'
        spell.push(l);     
    }
    else{
        l='zero'
        spell.push(l); 
    }
    //spell.push();
//console.log(spell);
//console.log(a[i]);

}
console.log(spell);