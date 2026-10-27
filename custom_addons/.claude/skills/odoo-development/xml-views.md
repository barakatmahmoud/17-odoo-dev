# XML / Views — Odoo 17

## Inspect First

Before editing XML:
- Locate the original view.
- Identify its external ID.
- Check inherited views.
- Inspect the exact XML structure.
- Check view inheritance priority if multiple inherited views affect the same element.

## XPath

Prefer small, stable XPath modifications.

Examples:

```xml
<xpath expr="//field[@name='employee_id']" position="attributes">
    <attribute name="readonly">state != 'draft'</attribute>
</xpath>
```

For a page:

```xml
<xpath expr="//page[@string='Salary']" position="attributes">
    <attribute name="readonly">state != 'draft'</attribute>
</xpath>
```

When the XML structure is ambiguous, search the codebase instead of guessing.

## Odoo 17 Modifiers

Use Odoo 17-compatible XML syntax.

For conditional UI behavior, verify:
- `invisible`
- `readonly`
- `required`
- `domain`
- `context`

Make sure field names and state values actually exist.

## View Inheritance

Do not replace an entire view if XPath can perform the requested change.

When multiple inherited views modify the same element:
- inspect their priorities
- understand application order
- avoid creating conflicting overrides

## Menus and Actions

Remember:
- domains belong to actions, not menu items directly
- menus reference actions
- inspect the linked action before changing record filtering

## Final Check

Verify:
- XML is well formed
- XPath matches the intended element
- referenced fields exist
- modifiers are valid
- no unrelated UI behavior changed
