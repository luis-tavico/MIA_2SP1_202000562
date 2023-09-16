
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD CADENA CAT CHGRP CHMOD CHOWN COMENTARIO CONT COPY DELETE DESTINO EDIT ENTERO EXECUTE FDISK FIND FIT GRP GUION ID IGUAL LOGIN LOGOUT MKDIR MKDISK MKFILE MKFS MKGRP MKUSR MOUNT MOVE NAME NOMBRE_ARCHIVO PASS PATH PAUSE R REMOVE RENAME REP RMDISK RMGRP RMUSR RUTA RUTA_ARCHIVO_ADSJ RUTA_ARCHIVO_TXT RUTA_CARPETA RUTA_DISCO RUTA_IMAGEN SIZE TYPE UGO UNIT UNMOUNT USERinstrucciones : instruccion instrucciones\n                     | instruccioninstruccion : comando parametros\n                   | comandocomando : MKDISK\n               | RMDISK\n               | FDISK\n               | MOUNT\n               | UNMOUNT\n               | MKFS\n               | LOGIN\n               | LOGOUT\n               | MKGRP\n               | RMGRP\n               | MKUSR\n               | RMUSR\n               | MKFILE\n               | CAT\n               | REMOVE\n               | EDIT\n               | RENAME\n               | MKDIR\n               | COPY\n               | MOVE\n               | FIND\n               | CHOWN\n               | CHGRP\n               | CHMOD\n               | PAUSE\n               | EXECUTE\n               | REP\n               | COMENTARIOparametros : parametro parametros\n                  | parametroparametro : argumento\n                 | opcionargumento : GUION param IGUAL valorparam : SIZE\n             | PATH\n             | FIT\n             | UNIT\n             | NAME\n             | TYPE\n             | DELETE\n             | ADD\n             | USER\n             | PASS\n             | ID\n             | GRP\n             | CONT\n             | DESTINO\n             | UGO\n             | RUTAvalor : ENTERO\n             | RUTA_ARCHIVO_TXT\n             | RUTA_IMAGEN\n             | RUTA_ARCHIVO_ADSJ\n             | RUTA_DISCO\n             | RUTA_CARPETA\n             | NOMBRE_ARCHIVO\n             | CADENAopcion : GUION R'
    
_lr_action_items = {'MKDISK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[4,4,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'RMDISK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[5,5,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'FDISK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[6,6,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'MOUNT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[7,7,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'UNMOUNT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[8,8,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'MKFS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[9,9,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'LOGIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[10,10,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'LOGOUT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[11,11,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'MKGRP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[12,12,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'RMGRP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[13,13,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'MKUSR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[14,14,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'RMUSR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[15,15,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'MKFILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[16,16,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'CAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[17,17,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'REMOVE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[18,18,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'EDIT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[19,19,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'RENAME':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[20,20,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'MKDIR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[21,21,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'COPY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[22,22,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'MOVE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[23,23,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'FIND':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[24,24,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'CHOWN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[25,25,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'CHGRP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[26,26,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'CHMOD':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[27,27,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'PAUSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[28,28,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'EXECUTE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[29,29,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'REP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[30,30,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'COMENTARIO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[31,31,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,58,59,60,61,62,63,64,65,66,],[0,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-1,-3,-34,-35,-36,-33,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'GUION':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,40,58,59,60,61,62,63,64,65,66,],[37,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,37,-35,-36,-62,-37,-54,-55,-56,-57,-58,-59,-60,-61,]),'R':([37,],[40,]),'SIZE':([37,],[41,]),'PATH':([37,],[42,]),'FIT':([37,],[43,]),'UNIT':([37,],[44,]),'NAME':([37,],[45,]),'TYPE':([37,],[46,]),'DELETE':([37,],[47,]),'ADD':([37,],[48,]),'USER':([37,],[49,]),'PASS':([37,],[50,]),'ID':([37,],[51,]),'GRP':([37,],[52,]),'CONT':([37,],[53,]),'DESTINO':([37,],[54,]),'UGO':([37,],[55,]),'RUTA':([37,],[56,]),'IGUAL':([39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,],[57,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,]),'ENTERO':([57,],[59,]),'RUTA_ARCHIVO_TXT':([57,],[60,]),'RUTA_IMAGEN':([57,],[61,]),'RUTA_ARCHIVO_ADSJ':([57,],[62,]),'RUTA_DISCO':([57,],[63,]),'RUTA_CARPETA':([57,],[64,]),'NOMBRE_ARCHIVO':([57,],[65,]),'CADENA':([57,],[66,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,2,],[1,32,]),'instruccion':([0,2,],[2,2,]),'comando':([0,2,],[3,3,]),'parametros':([3,34,],[33,38,]),'parametro':([3,34,],[34,34,]),'argumento':([3,34,],[35,35,]),'opcion':([3,34,],[36,36,]),'param':([37,],[39,]),'valor':([57,],[58,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones','gramatica.py',139),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','gramatica.py',140),
  ('instruccion -> comando parametros','instruccion',2,'p_instruccion','gramatica.py',145),
  ('instruccion -> comando','instruccion',1,'p_instruccion','gramatica.py',146),
  ('comando -> MKDISK','comando',1,'p_comando','gramatica.py',151),
  ('comando -> RMDISK','comando',1,'p_comando','gramatica.py',152),
  ('comando -> FDISK','comando',1,'p_comando','gramatica.py',153),
  ('comando -> MOUNT','comando',1,'p_comando','gramatica.py',154),
  ('comando -> UNMOUNT','comando',1,'p_comando','gramatica.py',155),
  ('comando -> MKFS','comando',1,'p_comando','gramatica.py',156),
  ('comando -> LOGIN','comando',1,'p_comando','gramatica.py',157),
  ('comando -> LOGOUT','comando',1,'p_comando','gramatica.py',158),
  ('comando -> MKGRP','comando',1,'p_comando','gramatica.py',159),
  ('comando -> RMGRP','comando',1,'p_comando','gramatica.py',160),
  ('comando -> MKUSR','comando',1,'p_comando','gramatica.py',161),
  ('comando -> RMUSR','comando',1,'p_comando','gramatica.py',162),
  ('comando -> MKFILE','comando',1,'p_comando','gramatica.py',163),
  ('comando -> CAT','comando',1,'p_comando','gramatica.py',164),
  ('comando -> REMOVE','comando',1,'p_comando','gramatica.py',165),
  ('comando -> EDIT','comando',1,'p_comando','gramatica.py',166),
  ('comando -> RENAME','comando',1,'p_comando','gramatica.py',167),
  ('comando -> MKDIR','comando',1,'p_comando','gramatica.py',168),
  ('comando -> COPY','comando',1,'p_comando','gramatica.py',169),
  ('comando -> MOVE','comando',1,'p_comando','gramatica.py',170),
  ('comando -> FIND','comando',1,'p_comando','gramatica.py',171),
  ('comando -> CHOWN','comando',1,'p_comando','gramatica.py',172),
  ('comando -> CHGRP','comando',1,'p_comando','gramatica.py',173),
  ('comando -> CHMOD','comando',1,'p_comando','gramatica.py',174),
  ('comando -> PAUSE','comando',1,'p_comando','gramatica.py',175),
  ('comando -> EXECUTE','comando',1,'p_comando','gramatica.py',176),
  ('comando -> REP','comando',1,'p_comando','gramatica.py',177),
  ('comando -> COMENTARIO','comando',1,'p_comando','gramatica.py',178),
  ('parametros -> parametro parametros','parametros',2,'p_parametros','gramatica.py',182),
  ('parametros -> parametro','parametros',1,'p_parametros','gramatica.py',183),
  ('parametro -> argumento','parametro',1,'p_parametro','gramatica.py',186),
  ('parametro -> opcion','parametro',1,'p_parametro','gramatica.py',187),
  ('argumento -> GUION param IGUAL valor','argumento',4,'p_argumento','gramatica.py',190),
  ('param -> SIZE','param',1,'p_param','gramatica.py',195),
  ('param -> PATH','param',1,'p_param','gramatica.py',196),
  ('param -> FIT','param',1,'p_param','gramatica.py',197),
  ('param -> UNIT','param',1,'p_param','gramatica.py',198),
  ('param -> NAME','param',1,'p_param','gramatica.py',199),
  ('param -> TYPE','param',1,'p_param','gramatica.py',200),
  ('param -> DELETE','param',1,'p_param','gramatica.py',201),
  ('param -> ADD','param',1,'p_param','gramatica.py',202),
  ('param -> USER','param',1,'p_param','gramatica.py',203),
  ('param -> PASS','param',1,'p_param','gramatica.py',204),
  ('param -> ID','param',1,'p_param','gramatica.py',205),
  ('param -> GRP','param',1,'p_param','gramatica.py',206),
  ('param -> CONT','param',1,'p_param','gramatica.py',207),
  ('param -> DESTINO','param',1,'p_param','gramatica.py',208),
  ('param -> UGO','param',1,'p_param','gramatica.py',209),
  ('param -> RUTA','param',1,'p_param','gramatica.py',210),
  ('valor -> ENTERO','valor',1,'p_valor','gramatica.py',214),
  ('valor -> RUTA_ARCHIVO_TXT','valor',1,'p_valor','gramatica.py',215),
  ('valor -> RUTA_IMAGEN','valor',1,'p_valor','gramatica.py',216),
  ('valor -> RUTA_ARCHIVO_ADSJ','valor',1,'p_valor','gramatica.py',217),
  ('valor -> RUTA_DISCO','valor',1,'p_valor','gramatica.py',218),
  ('valor -> RUTA_CARPETA','valor',1,'p_valor','gramatica.py',219),
  ('valor -> NOMBRE_ARCHIVO','valor',1,'p_valor','gramatica.py',220),
  ('valor -> CADENA','valor',1,'p_valor','gramatica.py',221),
  ('opcion -> GUION R','opcion',2,'p_opcion','gramatica.py',225),
]
