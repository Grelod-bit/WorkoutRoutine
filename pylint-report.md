************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:5:0: E0401: Unable to import 'flask' (import-error)
app.py:6:0: E0401: Unable to import 'flask' (import-error)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:44:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:59:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:87:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:123:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:145:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:182:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:182:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:202:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:212:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:231:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:236:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:260:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:260:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:281:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
db.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:25:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
users.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module workouts
workouts.py:1:0: C0114: Missing module docstring (missing-module-docstring)
workouts.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:61:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:76:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:85:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:95:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:102:0: C0116: Missing function or method docstring (missing-function-docstring)
workouts.py:110:0: C0116: Missing function or method docstring (missing-function-docstring)


## Docstring
```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
```
this app implementation doesn't use docstrings.

## Import

```
app.py:5:0: E0401: Unable to import 'flask' (import-error)
app.py:6:0: E0401: Unable to import 'flask' (import-error)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
```
pylint is giving these errors and so is vscode's pylance, but it is unjustified.


## Missing return value

```
app.py:250:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:292:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

Error is irrelevant since it is only present in the functions that have `GET`, `POST` or `request.method` 

## Constant name

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Irrelevant. Looks better lower-case.

## Dangerous default value

```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

```python
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```

Irrelevant, since this exact code will never change the list given as a default value.
