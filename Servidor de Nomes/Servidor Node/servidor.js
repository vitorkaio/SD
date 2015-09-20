    var http = require('http');
    var url = require('url'); 

    http.createServer(function(req,res) {
      res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' }); 
      
      var ur = url.parse(req.url, true).query;
      var l = JSON.stringify(ur);
      var number = l.split('"');

      var r = '';

      if(req.url.search('soma') != -1){

           var a = number[3];
           var b = number[7];
           r = 'Soma de ' + a + ' + ' + b + ' = ' + soma(parseInt(a), parseInt(b));     

      }

      else if(req.url.search('fat') != -1){

           var a = number[3];
           r = 'Fatorial de ' + a + ' = ' + fat(parseInt(a));


      }

      else if(req.url.search('ex') != -1){

           var a = number[3];
           var b = number[7];
           r = a + ' elevado ' + b + ' = ' + ex(a, b);
    }


      res.end(r + '');

    }).listen(3000);

    function soma(numeroUm, numeroDois){

       return numeroUm + numeroDois;
    }

    function fat(numero){

       var contador = numero;
       var res = 1;

       while(contador > 0){

            res *= contador;
            contador--;

      }

       return res;
    }

    function ex(base, x){

        return Math.pow(base, x);

    }

    console.log('Servidor iniciado em localhost:3000. Ctrl+C para encerrar…');

