# Fixer

Types:

```python
from benchify.types import FixerRunResponse
```

Methods:

- <code title="post /v1/fixer">client.fixer.<a href="./src/benchify/resources/fixer.py">run</a>(\*\*<a href="src/benchify/types/fixer_run_params.py">params</a>) -> <a href="./src/benchify/types/fixer_run_response.py">FixerRunResponse</a></code>

# Stacks

Types:

```python
from benchify.types import (
    StackCreateResponse,
    StackRetrieveResponse,
    StackUpdateResponse,
    StackCreateAndRunResponse,
    StackExecuteCommandResponse,
    StackGetLogsResponse,
    StackGetNetworkInfoResponse,
    StackReadFileResponse,
    StackResetResponse,
    StackWaitForDevServerURLResponse,
    StackWriteFileResponse,
)
```

Methods:

- <code title="post /v1/stacks">client.stacks.<a href="./src/benchify/resources/stacks.py">create</a>(\*\*<a href="src/benchify/types/stack_create_params.py">params</a>) -> <a href="./src/benchify/types/stack_create_response.py">StackCreateResponse</a></code>
- <code title="get /v1/stacks/{id}">client.stacks.<a href="./src/benchify/resources/stacks.py">retrieve</a>(id) -> <a href="./src/benchify/types/stack_retrieve_response.py">StackRetrieveResponse</a></code>
- <code title="post /v1/stacks/{id}/patch">client.stacks.<a href="./src/benchify/resources/stacks.py">update</a>(id, \*\*<a href="src/benchify/types/stack_update_params.py">params</a>) -> <a href="./src/benchify/types/stack_update_response.py">StackUpdateResponse</a></code>
- <code title="post /v1/stacks/create-and-run">client.stacks.<a href="./src/benchify/resources/stacks.py">create_and_run</a>(\*\*<a href="src/benchify/types/stack_create_and_run_params.py">params</a>) -> <a href="./src/benchify/types/stack_create_and_run_response.py">StackCreateAndRunResponse</a></code>
- <code title="delete /v1/stacks/{id}">client.stacks.<a href="./src/benchify/resources/stacks.py">destroy</a>(id) -> None</code>
- <code title="post /v1/stacks/{id}/exec">client.stacks.<a href="./src/benchify/resources/stacks.py">execute_command</a>(id, \*\*<a href="src/benchify/types/stack_execute_command_params.py">params</a>) -> <a href="./src/benchify/types/stack_execute_command_response.py">StackExecuteCommandResponse</a></code>
- <code title="get /v1/stacks/{id}/logs">client.stacks.<a href="./src/benchify/resources/stacks.py">get_logs</a>(id, \*\*<a href="src/benchify/types/stack_get_logs_params.py">params</a>) -> <a href="./src/benchify/types/stack_get_logs_response.py">StackGetLogsResponse</a></code>
- <code title="get /v1/stacks/{id}/network-info">client.stacks.<a href="./src/benchify/resources/stacks.py">get_network_info</a>(id) -> <a href="./src/benchify/types/stack_get_network_info_response.py">StackGetNetworkInfoResponse</a></code>
- <code title="get /v1/stacks/{id}/read-file">client.stacks.<a href="./src/benchify/resources/stacks.py">read_file</a>(id, \*\*<a href="src/benchify/types/stack_read_file_params.py">params</a>) -> <a href="./src/benchify/types/stack_read_file_response.py">StackReadFileResponse</a></code>
- <code title="post /v1/stacks/{id}/reset">client.stacks.<a href="./src/benchify/resources/stacks.py">reset</a>(id, \*\*<a href="src/benchify/types/stack_reset_params.py">params</a>) -> <a href="./src/benchify/types/stack_reset_response.py">StackResetResponse</a></code>
- <code title="get /v1/stacks/{id}/wait-url">client.stacks.<a href="./src/benchify/resources/stacks.py">wait_for_dev_server_url</a>(id, \*\*<a href="src/benchify/types/stack_wait_for_dev_server_url_params.py">params</a>) -> <a href="./src/benchify/types/stack_wait_for_dev_server_url_response.py">StackWaitForDevServerURLResponse</a></code>
- <code title="post /v1/stacks/{id}/write-file">client.stacks.<a href="./src/benchify/resources/stacks.py">write_file</a>(id, \*\*<a href="src/benchify/types/stack_write_file_params.py">params</a>) -> <a href="./src/benchify/types/stack_write_file_response.py">StackWriteFileResponse</a></code>

# FixStringLiterals

Types:

```python
from benchify.types import FixStringLiteralCreateResponse
```

Methods:

- <code title="post /v1/fix-string-literals">client.fix_string_literals.<a href="./src/benchify/resources/fix_string_literals.py">create</a>(\*\*<a href="src/benchify/types/fix_string_literal_create_params.py">params</a>) -> <a href="./src/benchify/types/fix_string_literal_create_response.py">FixStringLiteralCreateResponse</a></code>

# ValidateTemplate

Types:

```python
from benchify.types import ValidateTemplateValidateResponse
```

Methods:

- <code title="post /v1/validate-template">client.validate_template.<a href="./src/benchify/resources/validate_template.py">validate</a>(\*\*<a href="src/benchify/types/validate_template_validate_params.py">params</a>) -> <a href="./src/benchify/types/validate_template_validate_response.py">ValidateTemplateValidateResponse</a></code>

# FixParsingAndDiagnose

Types:

```python
from benchify.types import FixParsingAndDiagnoseDetectIssuesResponse
```

Methods:

- <code title="post /v1/fix-parsing-and-diagnose">client.fix_parsing_and_diagnose.<a href="./src/benchify/resources/fix_parsing_and_diagnose.py">detect_issues</a>(\*\*<a href="src/benchify/types/fix_parsing_and_diagnose_detect_issues_params.py">params</a>) -> <a href="./src/benchify/types/fix_parsing_and_diagnose_detect_issues_response.py">FixParsingAndDiagnoseDetectIssuesResponse</a></code>

# Fix

Types:

```python
from benchify.types import FixCreateAIFallbackResponse
```

Methods:

- <code title="post /v1/fix/ai-fallback">client.fix.<a href="./src/benchify/resources/fix/fix.py">create_ai_fallback</a>(\*\*<a href="src/benchify/types/fix_create_ai_fallback_params.py">params</a>) -> <a href="./src/benchify/types/fix_create_ai_fallback_response.py">FixCreateAIFallbackResponse</a></code>

## Standard

Types:

```python
from benchify.types.fix import StandardCreateResponse
```

Methods:

- <code title="post /v1/fix-standard">client.fix.standard.<a href="./src/benchify/resources/fix/standard.py">create</a>(\*\*<a href="src/benchify/types/fix/standard_create_params.py">params</a>) -> <a href="./src/benchify/types/fix/standard_create_response.py">StandardCreateResponse</a></code>
