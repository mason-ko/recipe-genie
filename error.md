ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/fastapi/applications.py", line 1133, in __call__
    await super().__call__(scope, receive, send)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/applications.py", line 113, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/middleware/sessions.py", line 85, in __call__
    await self.app(scope, receive, send_wrapper)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/routing.py", line 716, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/routing.py", line 736, in app
    await route.handle(scope, receive, send)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/routing.py", line 290, in handle
    await self.app(scope, receive, send)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/fastapi/routing.py", line 123, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/fastapi/routing.py", line 109, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/fastapi/routing.py", line 389, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/fastapi/routing.py", line 288, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/dev/my/recipe-genie/backend/app/api/recipes.py", line 27, in generate_recipe
    recipe_text = gemini.generate_recipe(
                  ^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/dev/my/recipe-genie/backend/app/services/gemini.py", line 17, in generate_recipe
    response = model.generate_content(prompt)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/google/generativeai/generative_models.py", line 331, in generate_content
    response = self._client.generate_content(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/google/ai/generativelanguage_v1beta/services/generative_service/client.py", line 835, in generate_content
    response = rpc(
               ^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/google/api_core/gapic_v1/method.py", line 131, in __call__
    return wrapped_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/google/api_core/retry/retry_unary.py", line 294, in retry_wrapped_func
    return retry_target(
           ^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/google/api_core/retry/retry_unary.py", line 156, in retry_target
    next_sleep = _retry_error_helper(
                 ^^^^^^^^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/google/api_core/retry/retry_base.py", line 214, in _retry_error_helper
    raise final_exc from source_exc
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/google/api_core/retry/retry_unary.py", line 147, in retry_target
    result = target()
             ^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/google/api_core/timeout.py", line 130, in func_with_timeout
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/yeongminko/.cache/pypoetry/virtualenvs/backend-HXHKy2u--py3.12/lib/python3.12/site-packages/google/api_core/grpc_helpers.py", line 77, in error_remapped_callable
    raise exceptions.from_grpc_error(exc) from exc
google.api_core.exceptions.NotFound: 404 models/gemini-pro is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.