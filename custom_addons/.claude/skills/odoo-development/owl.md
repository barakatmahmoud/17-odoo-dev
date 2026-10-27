# OWL / JavaScript — Odoo 17

## Investigation

Before changing frontend behavior:
- Find the OWL component.
- Find its XML template.
- Inspect registered components/services.
- Search for the event handler or RPC call.
- Check assets and module dependencies.
- Search for existing patches/extensions.

## Rules

Prefer the smallest frontend change.

Use Odoo 17 OWL conventions and existing services/components.

Do not introduce custom JavaScript if Python/XML can solve the requirement cleanly.

## Debugging Frontend Behavior

Trace:
1. UI element
2. template condition
3. component state
4. event handler
5. service/RPC
6. backend method
7. returned data
8. state update

If a button appears for the wrong record/user, inspect the source of the state/data instead of only changing the template.

## Patching

When extending an existing Odoo component:
- inspect the original implementation
- use the supported patch/extension mechanism
- preserve existing behavior
- avoid replacing large components unnecessarily

## Verification

Check:
- JavaScript syntax
- template syntax
- asset loading
- registry names
- service names
- state updates
- browser console errors
- backend RPC compatibility
