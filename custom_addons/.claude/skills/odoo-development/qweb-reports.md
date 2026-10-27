# QWeb Reports — Odoo 17

## Investigation

For a report issue, inspect all of:
1. `ir.actions.report`
2. report model
3. QWeb template
4. inherited templates
5. paper format if relevant
6. helper methods used by the template
7. report data/context

## Template Rules

Use valid QWeb syntax:

```xml
<t t-foreach="docs" t-as="doc">
    <span t-esc="doc.name"/>
</t>
```

For attributes:

```xml
<span t-att-class="doc.state"/>
```

For conditions:

```xml
<t t-if="doc.state == 'done'">
    ...
</t>
```

## Debugging

If a value prints as zero, empty, or incorrect:
- verify the record being passed
- verify the method being called
- verify method arguments
- inspect the return value
- inspect related fields
- check whether the method depends on context/company/user
- check whether a computed field is up to date

Do not assume the QWeb template is the root cause.

## Best Practice

Keep business logic in Python when practical. QWeb should primarily render prepared data.

## Verification

Check:
- template inheritance
- variable scope
- field existence
- method existence
- report action/model alignment
- formatting and pagination where relevant
