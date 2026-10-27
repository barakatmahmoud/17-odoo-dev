# Workflow / States / Approvals — Odoo 17

## Investigation

Before changing workflow behavior:
- Find the state/selection field.
- Search all assignments to that field.
- Find every button/action that changes state.
- Inspect approval methods.
- Inspect access groups.
- Inspect related wizards.
- Inspect inherited workflow logic.

## State Changes

Never assume the workflow is controlled by one method.

Search for:
- `state =`
- `write({'state':`
- `action_`
- approval methods
- server actions
- automated actions
- cron jobs

## Previous Stage / Return Logic

If a record can return to a previous stage:
- determine which stages are allowed
- exclude forbidden stages explicitly
- make sure the target stage is actually a previous/valid stage
- preserve the workflow sequence
- capture a return reason if required
- keep audit/history behavior consistent if the module has it

## Selection Fields

If using `selection_add`, inspect how the project orders stages.

Do not assume Python declaration order alone controls every workflow/UI ordering requirement.

Check:
- existing selection definition
- `selection_add`
- sequence fields if the workflow uses them
- statusbar configuration
- views
- transition logic

## Approval Logic

For approval levels:
- identify each approval state
- identify who can approve
- identify who can reject/return
- verify button visibility
- verify backend authorization
- do not rely only on UI visibility for security

## Wizards

For popup/wizard actions:
- inspect `TransientModel`
- inspect context
- inspect `active_model` and `active_ids`
- validate selected target stage
- validate required reason
- make sure the wizard modifies the intended record(s)

## Verification

Test:
- normal forward transition
- return transition
- forbidden transitions
- permissions
- multiple records if supported
- wizard behavior
- final states
