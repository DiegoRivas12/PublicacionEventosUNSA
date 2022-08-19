El primer estilo es Monolítico, donde el programa es
no se subdivide en funciones. En cambio, la lógica es
solo en una larga secuencia de declaraciones.

El segundo estilo Cookbook, la lógica se divide
en funciones, pero todas las funciones operan en compartido
variables globales.

Ejemplo controlesRivas/main.py (En este ejemplo se usa el estilo un o y dos)




```
@app.route('/showSignin')
def showSignin():
    if session.get('user'):#Si la sesion del usuario sigue activa ingresamos
        return render_template('usuarioNormal.html')
    else:
        return render_template('signin.html')#Ingresamois con nuestro usuario

@app.route('/usuarioNormal')
def usuarioNormal():
    if session.get('user'):
        return render_template('usuarioNormal.html')
    else:
        return render_template('error.html',error = 'Acceso No Autorizado')

@app.route('/usuarioVip')
def usuarioVip():
    if session.get('user'):
        return render_template('usuarioVip.html')
    else:
        return render_template('error.html',error = 'Acceso No Autorizado')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

```


En el tercer estilo, llamado Pipeline, las funciones
no se comunique utilizando datos globales. En cambio, ellos
recibir entrada y producir salida. El programa
luego se convierte en una larga cadena de llamadas a funciones.


Ejemplo controlesRivas/proce.sql (En este ejemplo se usa el estilo tres)
```
USE UNSA;
#DROP FUNCTION esNormal;
DELIMITER $$
create definer=`root`@`localhost` function esNormal(
_id_usuario INT)RETURNS INT DETERMINISTIC
begin

    DECLARE bandera BOOL;
    
    DECLARE aux INT;
    
    SET bandera = (SELECT COUNT(c.id_usuario) FROM UsuarioNormal c 
        INNER JOIN  Usuario p WHERE c.id_usuario = _id_usuario AND p.id_usuario = c.id_usuario
        GROUP BY c.id_usuario);
    IF bandera THEN
       SET aux = 1;
	ELSE
       SET aux = 0;
     END IF;
    
    RETURN aux;
    
end$$

DELIMITER ;

USE UNSA;
#DROP PROCEDURE validarLogin;


DELIMITER $$
create definer=`root`@`localhost` procedure validarLogin(
IN n_usuario varchar(30))
begin

    SELECT p.id_usuario id_usuario, p.Nombre Nombre, p.ApellidoPaterno, p.ApellidoMaterno, 
           p.Correo Correo,p.Telefono Telefono, p._usuario _usuario,
           p.contra contra, esNormal(p.id_usuario) sies
	FROM Usuario p INNER JOIN UsuarioNormal c
    ON p._usuario = n_usuario;
    
end$$

DELIMITER ;

```
