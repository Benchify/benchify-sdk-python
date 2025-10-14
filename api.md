# Shared Types

```python
from benchify.types import ResponseMeta
```

# Fixer

Types:

```python
from benchify.types import DiagnosticResponse, FixerFile, FixerRunResponse
```

Methods:

- <code title="post /v1/fixer">client.fixer.<a href="./src/benchify/resources/fixer.py">run</a>(\*\*<a href="src/benchify/types/fixer_run_params.py">params</a>) -> <a href="./src/benchify/types/fixer_run_response.py">FixerRunResponse</a></code>

# Sandboxes

Types:

```python
from benchify.types import SandboxCreateResponse, SandboxRetrieveResponse, SandboxUpdateResponse
```

Methods:

- <code title="post /sandboxes">client.sandboxes.<a href="./src/benchify/resources/sandboxes.py">create</a>(\*\*<a href="src/benchify/types/sandbox_create_params.py">params</a>) -> <a href="./src/benchify/types/sandbox_create_response.py">SandboxCreateResponse</a></code>
- <code title="get /sandboxes/{id}">client.sandboxes.<a href="./src/benchify/resources/sandboxes.py">retrieve</a>(id) -> <a href="./src/benchify/types/sandbox_retrieve_response.py">SandboxRetrieveResponse</a></code>
- <code title="post /sandboxes/{id}:patch">client.sandboxes.<a href="./src/benchify/resources/sandboxes.py">update</a>(id, \*\*<a href="src/benchify/types/sandbox_update_params.py">params</a>) -> <a href="./src/benchify/types/sandbox_update_response.py">SandboxUpdateResponse</a></code>
- <code title="delete /sandboxes/{id}">client.sandboxes.<a href="./src/benchify/resources/sandboxes.py">delete</a>(id) -> None</code>
