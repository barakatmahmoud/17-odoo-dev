# Python / ORM — Odoo 17

## Inspect First

Before modifying Python:
- Find the model definition.
- Find inherited classes.
- Search for overrides of the target method.
- Check field definitions and relations.
- Search for similar business logic.

## ORM Guidelines

Use standard Odoo APIs:
- `create()`
- `write()`
- `unlink()`
- `search()`
- `search_count()`
- `browse()`
- `mapped()`
- `filtered()`
- `ensure_one()`
- `@api.depends`
- `@api.constrains`
- `@api.onchange`

### create()

Preserve existing behavior:

```python
@api.model
def create(self, vals):
    record = super().create(vals)
    # requested logic
    return record
```

If the logic must affect values before creation, modify `vals` before `super()`.

### write()

Remember that `write()` can be called on multiple records:

```python
def write(self, vals):
    result = super().write(vals)
    # requested logic
    return result
```

Do not assume `self` is a singleton unless explicitly guaranteed.

## Constraints

Use `@api.constrains` for backend business validation that must run on create/write.

Always consider whether the validation should:
- ignore the current record
- check multiple records
- handle missing fields
- compare date boundaries
- check specific states

## Computed Fields

Verify:
- `store=True` or non-stored
- all dependencies in `@api.depends`
- related-field dependencies
- recomputation behavior

Avoid expensive searches inside loops when an efficient recordset/domain solution is possible.

## Performance

Avoid unnecessary queries such as:

```python
for employee in employees:
    self.env['hr.leave'].search(...)
```

when the operation can be efficiently batched.

Do not over-engineer simple requirements.

## Error Handling

Use appropriate Odoo exceptions:
- `ValidationError` for invalid business data
- `UserError` for user-facing business restrictions
- `AccessError` when access is genuinely involved

Messages should be clear and actionable.

## Important

Do not fix an ORM problem by blindly adding `sudo()`.
Do not use raw SQL unless ORM is unsuitable and there is a clear reason.
