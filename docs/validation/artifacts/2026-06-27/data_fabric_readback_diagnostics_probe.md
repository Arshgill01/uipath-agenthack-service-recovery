# Data Fabric Readback Diagnostics Probe

Date: 2026-06-27

Scope: read-only diagnostics for legacy snake_case and validated PascalCase Data Fabric audit storage.

## Scratch mutation decision

No scratch Data Fabric entity was created. Data Fabric entity system names must use letters/digits/underscores and cannot start with the required cloud scratch prefix `PFPROBE-20260627-`; mutating the validated V2 entity or legacy records would violate the guardrails, and deleting scratch cloud resources is out of scope. Proceeded with CLI/doc readback probes.


## `uip --version`

```text
1.195.1

(exit 0)
```

## `uip login status --output json`

```text
{
  "Result": "Success",
  "Code": "LoginStatus",
  "Data": {
    "Status": "Logged in",
    "BaseUrl": "https://cloud.uipath.com",
    "Organization": "keepingitlowkey",
    "OrganizationId": "2f5e2d22-41f9-4a73-ba72-a4142607ee72",
    "Tenant": "DefaultTenant",
    "TenantId": "ce9f6b89-4e70-47ee-a0b3-8bc4986b8772",
    "ExpirationDate": "2026-06-27T19:15:22.000Z"
  }
}

(exit 0)
```

## `uip tools list --output json`

```text
{
  "Result": "Success",
  "Code": "ToolList",
  "Data": [
    {
      "Name": "solution-tool",
      "Version": "1.195.0",
      "Description": "Create, pack, publish, and deploy UiPath Automation Solutions.",
      "CommandPrefix": "solution"
    },
    {
      "Name": "codedapp-tool",
      "Version": "1.195.0",
      "Description": "Build, pack, publish, deploy, and manage UiPath Coded Web Applications.",
      "CommandPrefix": "codedapp"
    },
    {
      "Name": "integrationservice-tool",
      "Version": "1.195.0",
      "Description": "Manage Integration Service connectors, connections, and triggers.",
      "CommandPrefix": "is"
    },
    {
      "Name": "orchestrator-tool",
      "Version": "1.195.0",
      "Description": "Manage Orchestrator folders, jobs, processes, and releases.",
      "CommandPrefix": "or"
    },
    {
      "Name": "rpa-tool",
      "Version": "1.195.1",
      "Description": "Tool for creating and managing UiPath RPA projects",
      "CommandPrefix": "rpa"
    },
    {
      "Name": "test-manager-tool",
      "Version": "1.195.0",
      "Description": "Manage test cases, test sets, executions, and results.",
      "CommandPrefix": "tm"
    },
    {
      "Name": "maestro-tool",
      "Version": "1.195.0",
      "Description": "Create, debug, and run Maestro projects and jobs.",
      "CommandPrefix": "maestro"
    },
    {
      "Name": "data-fabric-tool",
      "Version": "1.195.0",
      "Description": "Manage Data Fabric entities and records.",
      "CommandPrefix": "df"
    },
    {
      "Name": "tasks-tool",
      "Version": "1.195.0",
      "Description": "Manage Action Center tasks.",
      "CommandPrefix": "tasks"
    },
    {
      "Name": "platform-tool",
      "Version": "1.195.0",
      "Description": "Manage UiPath platform-level resources such as tenant licensing.",
      "CommandPrefix": "platform"
    }
  ]
}

(exit 0)
```

## `uip df --help`

```text
                                     uip df                                     
       Manage Data Fabric entity schemas, records, and file attachments.        
                Use --help with nested commands for more detail.                

┌─ Usage ──────────────────────────────────────────────────────────────────────┐
│ uip df [options] [command]                                                   │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Commands ───────────────────────────────────────────────────────────────────┐
│ choice-set-values   Manage the individual values of a Data Fabric choice     │
│                     set. Use 'df choice-sets list-values <choice-set-id>' to │
│                     list existing values and their IDs.                      │
│ choice-sets         Manage Data Fabric choice sets — the enumerated value    │
│                     lists referenced by                                      │
│                     CHOICE_SET_SINGLE/CHOICE_SET_MULTIPLE entity fields. Use │
│                     'list'/'list-values' to inspect, and                     │
│                     'create'/'update'/'delete' to manage them. Manage        │
│                     individual values with 'df choice-set-values'.           │
│ entities            Browse Data Fabric entity schemas                        │
│ files               Manage file attachments on Data Fabric entity records    │
│ help                display help for command                                 │
│ records             Manage Data Fabric entity records                        │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Options ────────────────────────────────────────────────────────────────────┐
│ -h, --help                     display help for command                      │
│ --output                       Output format (default: json)                 │
│ <table|json|yaml|plain>                                                      │
│ --output-filter <expression>   JMESPath expression applied to the Data field │
│                                of the response envelope                      │
│ --log-level                    Log level threshold (default: info)           │
│ <debug|info|warn|error>                                                      │
│ --log-file <path>              Write logs to file instead of stderr          │
└──────────────────────────────────────────────────────────────────────────────┘

(exit 0)
```

## `uip df entities --help`

```text
                                uip df entities                                 
                       Browse Data Fabric entity schemas                        
                Use --help with nested commands for more detail.                

┌─ Usage ──────────────────────────────────────────────────────────────────────┐
│ uip df entities [options] [command]                                          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Commands ───────────────────────────────────────────────────────────────────┐
│ create   Create a new Data Fabric entity                                     │
│ delete   Delete a Data Fabric entity (irreversible)                          │
│ get      Get schema details of a Data Fabric entity                          │
│ help     display help for command                                            │
│ list     List all Data Fabric entities                                       │
│ update   Update schema or metadata of a Data Fabric entity                   │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Options ────────────────────────────────────────────────────────────────────┐
│ -h, --help                     display help for command                      │
│ --output                       Output format (default: json)                 │
│ <table|json|yaml|plain>                                                      │
│ --output-filter <expression>   JMESPath expression applied to the Data field │
│                                of the response envelope                      │
│ --log-level                    Log level threshold (default: info)           │
│ <debug|info|warn|error>                                                      │
│ --log-file <path>              Write logs to file instead of stderr          │
└──────────────────────────────────────────────────────────────────────────────┘

(exit 0)
```

## `uip df entities get --help`

```text
                              uip df entities get                               
                   Get schema details of a Data Fabric entity                   
                Use --help with nested commands for more detail.                

┌─ Usage ──────────────────────────────────────────────────────────────────────┐
│ uip df entities get [options] <id>                                           │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Arguments ──────────────────────────────────────────────────────────────────┐
│ id   Entity ID                                                               │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Options ────────────────────────────────────────────────────────────────────┐
│ -h, --help                     display help for command                      │
│ --output                       Output format (default: json)                 │
│ <table|json|yaml|plain>                                                      │
│ --output-filter <expression>   JMESPath expression applied to the Data field │
│                                of the response envelope                      │
│ --log-level                    Log level threshold (default: info)           │
│ <debug|info|warn|error>                                                      │
│ --log-file <path>              Write logs to file instead of stderr          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Examples ───────────────────────────────────────────────────────────────────┐
│ Get entity schema by ID.                                                     │
│                                                                              │
│   $ uip df entities get a1b2c3d4-0000-0000-0000-000000000001                 │
│                                                                              │
│   id             a1b2c3d4-0000-0000-0000-000000000001                        │
│   name           Invoice                                                     │
│   displayName    Invoice                                                     │
│   entityType     Standard                                                    │
│   description    Invoice records                                             │
│   isRbacEnabled  false                                                       │
│   fields:                                                                    │
│     id        name  dis…  fie…  sqlType   isR…  isU…  isE…  isR…  isP…  isS… │
│     ────────  ────  ────  ────  ────────  ────  ────  ────  ────  ────  ──── │
│     f100000…  amo…  Amo…  {"n…  {"name"…  true  fal…  fal…  fal…  fal…  fal… │
└──────────────────────────────────────────────────────────────────────────────┘

(exit 0)
```

## `uip df records insert --help`

```text
                             uip df records insert                              
                    Insert records into a Data Fabric entity                    
                Use --help with nested commands for more detail.                

┌─ Usage ──────────────────────────────────────────────────────────────────────┐
│ uip df records insert [options] <id>                                         │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Arguments ──────────────────────────────────────────────────────────────────┐
│ id   Entity ID                                                               │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Options ────────────────────────────────────────────────────────────────────┐
│ -f, --file <path>              Path to JSON file with record data (object or │
│                                array of objects)                             │
│ --body <json>                  Inline JSON record data (object or array of   │
│                                objects)                                      │
│ -h, --help                     display help for command                      │
│ --output                       Output format (default: json)                 │
│ <table|json|yaml|plain>                                                      │
│ --output-filter <expression>   JMESPath expression applied to the Data field │
│                                of the response envelope                      │
│ --log-level                    Log level threshold (default: info)           │
│ <debug|info|warn|error>                                                      │
│ --log-file <path>              Write logs to file instead of stderr          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Examples ───────────────────────────────────────────────────────────────────┐
│ Insert a record                                                              │
│                                                                              │
│   $ uip df records insert a1b2c3d4-0000-0000-0000-000000000001 --body '{"amount":1500,"status":"New"}' │
│                                                                              │
│   Id      b2c3d4e5-0000-0000-0000-000000000010                               │
│   amount  1500                                                               │
│   status  New                                                                │
│                                                                              │
│ Insert a record into an entity that has choice-set and relationship fields.  │
│ CHOICE_SET_SINGLE → pass the choice value's 'numberId' (integer, NOT the     │
│ name string — look it up via 'df choice-sets list-values <id>').             │
│ CHOICE_SET_MULTIPLE → pass an array of numberId integers. RELATIONSHIP →     │
│ always pass the target record's Id (UUID), regardless of which               │
│ 'referenceFieldId' the schema uses for the join (the referenceFieldId        │
│ configures the join, not the stored value).                                  │
│                                                                              │
│   $ uip df records insert a1b2c3d4-0000-0000-0000-000000000004 --body '{"category":0,"tags":[1,3],"submitter":"e1f2a3b4-0000-0000-0000-000000000001","amount":250}' │
│                                                                              │
│   Id         b2c3d4e5-0000-0000-0000-000000000020                            │
│   category   0                                                               │
│   tags       1, 3                                                            │
│   submitter  e1f2a3b4-0000-0000-0000-000000000001                            │
│   amount     250                                                             │
└──────────────────────────────────────────────────────────────────────────────┘

(exit 0)
```

## `uip df records update --help`

```text
                             uip df records update                              
                     Update records in a Data Fabric entity                     
                Use --help with nested commands for more detail.                

┌─ Usage ──────────────────────────────────────────────────────────────────────┐
│ uip df records update [options] <id>                                         │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Arguments ──────────────────────────────────────────────────────────────────┐
│ id   Entity ID                                                               │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Options ────────────────────────────────────────────────────────────────────┐
│ -f, --file <path>              Path to JSON file with record data (must      │
│                                include Id field)                             │
│ --body <json>                  Inline JSON record data (must include Id      │
│                                field)                                        │
│ -h, --help                     display help for command                      │
│ --output                       Output format (default: json)                 │
│ <table|json|yaml|plain>                                                      │
│ --output-filter <expression>   JMESPath expression applied to the Data field │
│                                of the response envelope                      │
│ --log-level                    Log level threshold (default: info)           │
│ <debug|info|warn|error>                                                      │
│ --log-file <path>              Write logs to file instead of stderr          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Examples ───────────────────────────────────────────────────────────────────┐
│ Update a record                                                              │
│                                                                              │
│   $ uip df records update a1b2c3d4-0000-0000-0000-000000000001 --body '{"Id":"b2c3d4e5-0000-0000-0000-000000000001","status":"Paid"}' │
│                                                                              │
│   Id      b2c3d4e5-0000-0000-0000-000000000001                               │
│   status  Paid                                                               │
└──────────────────────────────────────────────────────────────────────────────┘

(exit 0)
```

## `uip df records query --help`

```text
                              uip df records query                              
Query records in a Data Fabric entity with filters, sorting, and aggregates. Provide a JSON object via --body or --file with optional keys: filterGroup, sortOptions (use isDescending: true/false), selectedFields, aggregates (function: COUNT/SUM/AVG/MIN/MAX, field, alias?), groupBy.
                Use --help with nested commands for more detail.                

┌─ Usage ──────────────────────────────────────────────────────────────────────┐
│ uip df records query [options] <id>                                          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Arguments ──────────────────────────────────────────────────────────────────┐
│ id   Entity ID                                                               │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Options ────────────────────────────────────────────────────────────────────┐
│ -f, --file <path>              Path to JSON file with query options          │
│                                (filterGroup, selectedFields, sortOptions,    │
│                                aggregates, groupBy)                          │
│ --body <json>                  Inline JSON query options (filterGroup,       │
│                                selectedFields, sortOptions, aggregates,      │
│                                groupBy)                                      │
│ -l, --limit <number>           Number of records to return per page          │
│ -o, --offset <number>          Start from the page containing this record    │
│                                index (rounded down to nearest page           │
│                                boundary;(mutually exclusive with --cursor)   │
│ --cursor <cursor>              Pagination cursor from a previous response to │
│                                fetch the next page                           │
│ -h, --help                     display help for command                      │
│ --output                       Output format (default: json)                 │
│ <table|json|yaml|plain>                                                      │
│ --output-filter <expression>   JMESPath expression applied to the Data field │
│                                of the response envelope                      │
│ --log-level                    Log level threshold (default: info)           │
│ <debug|info|warn|error>                                                      │
│ --log-file <path>              Write logs to file instead of stderr          │
└──────────────────────────────────────────────────────────────────────────────┘

(exit 0)
```

## `uip df records get --help`

```text
                               uip df records get                               
                           Get a single record by ID                            
                Use --help with nested commands for more detail.                

┌─ Usage ──────────────────────────────────────────────────────────────────────┐
│ uip df records get [options] <id> <key>                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Arguments ──────────────────────────────────────────────────────────────────┐
│ id    Entity ID                                                              │
│ key   Record ID                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Options ────────────────────────────────────────────────────────────────────┐
│ -h, --help                     display help for command                      │
│ --output                       Output format (default: json)                 │
│ <table|json|yaml|plain>                                                      │
│ --output-filter <expression>   JMESPath expression applied to the Data field │
│                                of the response envelope                      │
│ --log-level                    Log level threshold (default: info)           │
│ <debug|info|warn|error>                                                      │
│ --log-file <path>              Write logs to file instead of stderr          │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ Examples ───────────────────────────────────────────────────────────────────┐
│ Get a record by ID                                                           │
│                                                                              │
│   $ uip df records get a1b2c3d4-0000-0000-0000-000000000001 b2c3d4e5-0000-0000-0000-000000000001 │
│                                                                              │
│   Id      b2c3d4e5-0000-0000-0000-000000000001                               │
│   amount  1500                                                               │
│   status  Paid                                                               │
└──────────────────────────────────────────────────────────────────────────────┘

(exit 0)
```

## `uip df entities list --native-only --output json`

```text
{
  "Result": "Success",
  "Code": "EntityList",
  "Data": [
    {
      "Name": "SystemUser",
      "DisplayName": "System Users",
      "EntityTypeId": 3,
      "EntityType": "SystemEntity",
      "Description": "Contains Automation Cloud users and groups that have ever had roles assigned, or accessed Data Service",
      "FolderId": "00000000-0000-0000-0000-000000000000",
      "Fields": [
        {
          "Id": "ecfb9f93-96ba-493d-ae84-0b50a76b1b85",
          "Name": "UpdateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "UpdateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:04.953Z",
          "UpdatedTime": "2026-06-25T15:37:04.953Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        },
        {
          "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
          "Name": "Name",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "Name",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:04.953Z",
          "UpdatedTime": "2026-06-25T15:37:04.953Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 512
          }
        },
        {
          "Id": "b0db4314-c83b-4b73-8543-35d9c138f84f",
          "Name": "IsActive",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "IsActive",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:04.953Z",
          "UpdatedTime": "2026-06-25T15:37:04.953Z",
          "FieldDataType": {
            "Name": "BOOLEAN"
          }
        },
        {
          "Id": "b00ebbbc-0767-4a0f-83f9-8e4e5e028570",
          "Name": "Id",
          "IsPrimaryKey": true,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "Id",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:04.953Z",
          "UpdatedTime": "2026-06-25T15:37:04.953Z",
          "FieldDataType": {
            "Name": "UUID"
          }
        },
        {
          "Id": "1f244ad1-bc9e-4798-9768-d18c987cb435",
          "Name": "Email",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "E-mail",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:04.953Z",
          "UpdatedTime": "2026-06-25T15:37:04.953Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 512
          }
        },
        {
          "Id": "a6b8416e-ef5c-457e-be90-d9e484596513",
          "Name": "CreateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:04.953Z",
          "UpdatedTime": "2026-06-25T15:37:04.953Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        },
        {
          "Id": "e14e2dcc-0611-4aa2-afa3-ea812a8cdb50",
          "Name": "Type",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceChoiceSet": {
            "Name": "UserType",
            "EntityTypeId": 0,
            "EntityType": "Entity",
            "FolderId": "00000000-0000-0000-0000-000000000000",
            "IsRbacEnabled": false,
            "IsInsightsEnabled": false,
            "InvalidIdentifiers": [],
            "IsModelReserved": false,
            "Id": "238ef8b6-ab70-f111-ac9a-002248a16d28"
          },
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "Type",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "FieldDisplayType": "ChoiceSetSingle",
          "ChoiceSetId": "238ef8b6-ab70-f111-ac9a-002248a16d28",
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:04.953Z",
          "UpdatedTime": "2026-06-25T15:37:04.953Z",
          "FieldDataType": {
            "Name": "CHOICE_SET_SINGLE",
            "MaxValue": 9007199254740991,
            "MinValue": -9007199254740991
          }
        }
      ],
      "RecordCount": 6,
      "StorageSizeInMB": 0.070312,
      "UsedStorageSizeInMB": 0.015625,
      "IsRbacEnabled": false,
      "IsInsightsEnabled": false,
      "InvalidIdentifiers": [],
      "IsModelReserved": false,
      "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28",
      "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "CreatedTime": "2026-06-25T15:37:04.94Z",
      "UpdatedTime": "2026-06-25T15:37:04.94Z"
    },
    {
      "Name": "ServiceRecoveryAuditBundle",
      "DisplayName": "Service Recovery Audit Bundle",
      "EntityTypeId": 0,
      "EntityType": "Entity",
      "Description": "Stores one governed service-recovery audit bundle for UiPath Maestro Case validation and demo reconstruction.",
      "FolderId": "00000000-0000-0000-0000-000000000000",
      "Fields": [
        {
          "Id": "3c8ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "case_id",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "case_id",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.143Z",
          "UpdatedTime": "2026-06-25T15:37:05.143Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "3d8ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "service_id",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "service_id",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.157Z",
          "UpdatedTime": "2026-06-25T15:37:05.157Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "3e8ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "scenario_id",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "scenario_id",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.17Z",
          "UpdatedTime": "2026-06-25T15:37:05.17Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 20
          }
        },
        {
          "Id": "3f8ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "audit_contract_version",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "audit_contract_version",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.183Z",
          "UpdatedTime": "2026-06-25T15:37:05.183Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "408ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "business_state",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "business_state",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.193Z",
          "UpdatedTime": "2026-06-25T15:37:05.193Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 50
          }
        },
        {
          "Id": "418ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "derived_evidence_state",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "derived_evidence_state",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.203Z",
          "UpdatedTime": "2026-06-25T15:37:05.203Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "428ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "closure_block_reason",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "closure_block_reason",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.213Z",
          "UpdatedTime": "2026-06-25T15:37:05.213Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "438ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "interpretation_policy_version",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "interpretation_policy_version",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.227Z",
          "UpdatedTime": "2026-06-25T15:37:05.227Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "448ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "decision_policy_version",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "decision_policy_version",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.237Z",
          "UpdatedTime": "2026-06-25T15:37:05.237Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "458ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "source_case_instance_key",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "source_case_instance_key",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.25Z",
          "UpdatedTime": "2026-06-25T15:37:05.25Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "468ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "source_task_id",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "source_task_id",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.26Z",
          "UpdatedTime": "2026-06-25T15:37:05.26Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 50
          }
        },
        {
          "Id": "478ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "package_version",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "package_version",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.27Z",
          "UpdatedTime": "2026-06-25T15:37:05.27Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 50
          }
        },
        {
          "Id": "488ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "raw_agent_event_json",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "raw_agent_event_json",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.283Z",
          "UpdatedTime": "2026-06-25T15:37:05.283Z",
          "FieldDataType": {
            "Name": "MULTILINE_TEXT",
            "LengthLimit": 10000
          }
        },
        {
          "Id": "498ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "policy_decision_event_json",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "policy_decision_event_json",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.307Z",
          "UpdatedTime": "2026-06-25T15:37:05.307Z",
          "FieldDataType": {
            "Name": "MULTILINE_TEXT",
            "LengthLimit": 10000
          }
        },
        {
          "Id": "4a8ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "reviewer_packet_json",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "reviewer_packet_json",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.32Z",
          "UpdatedTime": "2026-06-25T15:37:05.32Z",
          "FieldDataType": {
            "Name": "MULTILINE_TEXT",
            "LengthLimit": 10000
          }
        },
        {
          "Id": "4b8ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "audit_bundle_json",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "audit_bundle_json",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.333Z",
          "UpdatedTime": "2026-06-25T15:37:05.333Z",
          "FieldDataType": {
            "Name": "MULTILINE_TEXT",
            "LengthLimit": 10000
          }
        },
        {
          "Id": "4c8ef8b6-ab70-f111-ac9a-002248a16d28",
          "Name": "created_at",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "created_at",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.343Z",
          "UpdatedTime": "2026-06-25T15:37:05.343Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ",
            "LengthLimit": 1000
          }
        },
        {
          "Id": "b1ca5bad-a8ff-486b-854f-7eefa61a8f51",
          "Name": "Id",
          "IsPrimaryKey": true,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "Id",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.07Z",
          "UpdatedTime": "2026-06-25T15:37:05.07Z",
          "FieldDataType": {
            "Name": "UUID"
          }
        },
        {
          "Id": "0fb8b9e4-8eed-4b84-acc6-98cac21e7df3",
          "Name": "UpdateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "UpdateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.07Z",
          "UpdatedTime": "2026-06-25T15:37:05.07Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        },
        {
          "Id": "e82195c2-76ec-4ada-a539-afc98913d012",
          "Name": "CreateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.07Z",
          "UpdatedTime": "2026-06-25T15:37:05.07Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        },
        {
          "Id": "8b27783e-fdd2-463f-8941-cb21985f56cc",
          "Name": "UpdatedBy",
          "IsPrimaryKey": false,
          "IsForeignKey": true,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceName": "fk_UpdatedBy_55331d30-1048-4517-8841-a0d600092302",
          "ReferenceEntity": {
            "Name": "SystemUser",
            "DisplayName": "System Users",
            "EntityTypeId": 3,
            "EntityType": "SystemEntity",
            "FolderId": "00000000-0000-0000-0000-000000000000",
            "IsRbacEnabled": false,
            "IsInsightsEnabled": false,
            "InvalidIdentifiers": [],
            "IsModelReserved": false,
            "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
          },
          "ReferenceField": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Definition": {
              "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
              "Name": "Name",
              "IsPrimaryKey": false,
              "IsForeignKey": false,
              "IsExternalField": false,
              "IsHiddenField": false,
              "FieldCategoryId": 0,
              "IsUnique": false,
              "ReferenceType": "ManyToOne",
              "IsRequired": false,
              "IsEncrypted": false,
              "DisplayName": "Name",
              "IsSystemField": false,
              "IsAttachment": false,
              "IsRbacEnabled": false,
              "IsModelReserved": false,
              "CreatedTime": "2026-06-25T15:37:04.953Z",
              "UpdatedTime": "2026-06-25T15:37:04.953Z",
              "FieldDataType": {
                "Name": "NVARCHAR",
                "LengthLimit": 512
              }
            }
          },
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "UpdatedBy",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "FieldDisplayType": "Relationship",
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.07Z",
          "UpdatedTime": "2026-06-25T15:37:05.07Z",
          "FieldDataType": {
            "Name": "RELATIONSHIP"
          }
        },
        {
          "Id": "3b33ee30-0542-42bb-a4b6-f1f18f2b1fb7",
          "Name": "CreatedBy",
          "IsPrimaryKey": false,
          "IsForeignKey": true,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceName": "fk_CreatedBy_5b269828-016f-4902-aa02-b11b8a456121",
          "ReferenceEntity": {
            "Name": "SystemUser",
            "DisplayName": "System Users",
            "EntityTypeId": 3,
            "EntityType": "SystemEntity",
            "FolderId": "00000000-0000-0000-0000-000000000000",
            "IsRbacEnabled": false,
            "IsInsightsEnabled": false,
            "InvalidIdentifiers": [],
            "IsModelReserved": false,
            "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
          },
          "ReferenceField": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Definition": {
              "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
              "Name": "Name",
              "IsPrimaryKey": false,
              "IsForeignKey": false,
              "IsExternalField": false,
              "IsHiddenField": false,
              "FieldCategoryId": 0,
              "IsUnique": false,
              "ReferenceType": "ManyToOne",
              "IsRequired": false,
              "IsEncrypted": false,
              "DisplayName": "Name",
              "IsSystemField": false,
              "IsAttachment": false,
              "IsRbacEnabled": false,
              "IsModelReserved": false,
              "CreatedTime": "2026-06-25T15:37:04.953Z",
              "UpdatedTime": "2026-06-25T15:37:04.953Z",
              "FieldDataType": {
                "Name": "NVARCHAR",
                "LengthLimit": 512
              }
            }
          },
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreatedBy",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "FieldDisplayType": "Relationship",
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-25T15:37:05.07Z",
          "UpdatedTime": "2026-06-25T15:37:05.07Z",
          "FieldDataType": {
            "Name": "RELATIONSHIP"
          }
        }
      ],
      "RecordCount": 30,
      "StorageSizeInMB": 0.140625,
      "UsedStorageSizeInMB": 0.03125,
      "IsRbacEnabled": false,
      "IsInsightsEnabled": false,
      "InvalidIdentifiers": [],
      "IsModelReserved": false,
      "Id": "328ef8b6-ab70-f111-ac9a-002248a16d28",
      "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "CreatedTime": "2026-06-25T15:37:05.057Z",
      "UpdatedTime": "2026-06-25T15:37:05.343Z"
    },
    {
      "Name": "TestEntity",
      "DisplayName": "Test Entity",
      "EntityTypeId": 0,
      "EntityType": "Entity",
      "Description": "",
      "FolderId": "00000000-0000-0000-0000-000000000000",
      "Fields": [
        {
          "Id": "73f26b58-3871-f111-ac9a-002248a16d28",
          "Name": "test_field",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "test_field",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T08:23:49.053Z",
          "UpdatedTime": "2026-06-26T08:23:49.053Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 200
          }
        },
        {
          "Id": "8f4cd38d-59da-403e-aa01-19a55d2b619a",
          "Name": "UpdateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "UpdateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T08:23:48.973Z",
          "UpdatedTime": "2026-06-26T08:23:48.973Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        },
        {
          "Id": "f5b4f829-2edf-42c1-907f-1a5ede4b8063",
          "Name": "UpdatedBy",
          "IsPrimaryKey": false,
          "IsForeignKey": true,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceName": "fk_UpdatedBy_12baaefd-78ba-438c-87e3-3e16c9b916b4",
          "ReferenceEntity": {
            "Name": "SystemUser",
            "DisplayName": "System Users",
            "EntityTypeId": 3,
            "EntityType": "SystemEntity",
            "FolderId": "00000000-0000-0000-0000-000000000000",
            "IsRbacEnabled": false,
            "IsInsightsEnabled": false,
            "InvalidIdentifiers": [],
            "IsModelReserved": false,
            "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
          },
          "ReferenceField": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Definition": {
              "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
              "Name": "Name",
              "IsPrimaryKey": false,
              "IsForeignKey": false,
              "IsExternalField": false,
              "IsHiddenField": false,
              "FieldCategoryId": 0,
              "IsUnique": false,
              "ReferenceType": "ManyToOne",
              "IsRequired": false,
              "IsEncrypted": false,
              "DisplayName": "Name",
              "IsSystemField": false,
              "IsAttachment": false,
              "IsRbacEnabled": false,
              "IsModelReserved": false,
              "CreatedTime": "2026-06-25T15:37:04.953Z",
              "UpdatedTime": "2026-06-25T15:37:04.953Z",
              "FieldDataType": {
                "Name": "NVARCHAR",
                "LengthLimit": 512
              }
            }
          },
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "UpdatedBy",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "FieldDisplayType": "Relationship",
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T08:23:48.973Z",
          "UpdatedTime": "2026-06-26T08:23:48.973Z",
          "FieldDataType": {
            "Name": "RELATIONSHIP"
          }
        },
        {
          "Id": "7670de0c-fd65-4ddf-815d-90cc96cd596c",
          "Name": "CreatedBy",
          "IsPrimaryKey": false,
          "IsForeignKey": true,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceName": "fk_CreatedBy_f6855ec4-303b-4472-af60-212079141eed",
          "ReferenceEntity": {
            "Name": "SystemUser",
            "DisplayName": "System Users",
            "EntityTypeId": 3,
            "EntityType": "SystemEntity",
            "FolderId": "00000000-0000-0000-0000-000000000000",
            "IsRbacEnabled": false,
            "IsInsightsEnabled": false,
            "InvalidIdentifiers": [],
            "IsModelReserved": false,
            "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
          },
          "ReferenceField": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Definition": {
              "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
              "Name": "Name",
              "IsPrimaryKey": false,
              "IsForeignKey": false,
              "IsExternalField": false,
              "IsHiddenField": false,
              "FieldCategoryId": 0,
              "IsUnique": false,
              "ReferenceType": "ManyToOne",
              "IsRequired": false,
              "IsEncrypted": false,
              "DisplayName": "Name",
              "IsSystemField": false,
              "IsAttachment": false,
              "IsRbacEnabled": false,
              "IsModelReserved": false,
              "CreatedTime": "2026-06-25T15:37:04.953Z",
              "UpdatedTime": "2026-06-25T15:37:04.953Z",
              "FieldDataType": {
                "Name": "NVARCHAR",
                "LengthLimit": 512
              }
            }
          },
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreatedBy",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "FieldDisplayType": "Relationship",
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T08:23:48.973Z",
          "UpdatedTime": "2026-06-26T08:23:48.973Z",
          "FieldDataType": {
            "Name": "RELATIONSHIP"
          }
        },
        {
          "Id": "cc736adb-8ddb-48bd-8d11-96cc46a5766e",
          "Name": "Id",
          "IsPrimaryKey": true,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "Id",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T08:23:48.973Z",
          "UpdatedTime": "2026-06-26T08:23:48.973Z",
          "FieldDataType": {
            "Name": "UUID"
          }
        },
        {
          "Id": "01544661-0bc9-40e5-9ba2-aaf51bdd7db7",
          "Name": "CreateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T08:23:48.973Z",
          "UpdatedTime": "2026-06-26T08:23:48.973Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        }
      ],
      "RecordCount": 3,
      "StorageSizeInMB": 0.140625,
      "UsedStorageSizeInMB": 0.03125,
      "IsRbacEnabled": false,
      "IsInsightsEnabled": false,
      "InvalidIdentifiers": [],
      "IsModelReserved": false,
      "Id": "69f26b58-3871-f111-ac9a-002248a16d28",
      "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "CreatedTime": "2026-06-26T08:23:48.95Z",
      "UpdatedTime": "2026-06-26T08:23:49.06Z"
    },
    {
      "Name": "DataFabricPascalProbe",
      "DisplayName": "Data Fabric Pascal Probe",
      "EntityTypeId": 0,
      "EntityType": "Entity",
      "Description": "Temporary validation entity for custom field readback behavior.",
      "FolderId": "00000000-0000-0000-0000-000000000000",
      "Fields": [
        {
          "Id": "99a39b80-4671-f111-ac9a-002248a16d28",
          "Name": "Title",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "Title",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:05:05.577Z",
          "UpdatedTime": "2026-06-26T10:05:05.577Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "9aa39b80-4671-f111-ac9a-002248a16d28",
          "Name": "CaseId",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "CaseId",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:05:05.59Z",
          "UpdatedTime": "2026-06-26T10:05:05.59Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "b1ed53f1-62ad-4ad8-bb54-37ff137b1c59",
          "Name": "UpdateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "UpdateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:05:05.473Z",
          "UpdatedTime": "2026-06-26T10:05:05.473Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        },
        {
          "Id": "8700f067-f59e-415d-9cd2-3860acd4bb76",
          "Name": "CreateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:05:05.473Z",
          "UpdatedTime": "2026-06-26T10:05:05.473Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        },
        {
          "Id": "86400f90-d7c6-4d9e-beec-6b15f88371b8",
          "Name": "Id",
          "IsPrimaryKey": true,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "Id",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:05:05.473Z",
          "UpdatedTime": "2026-06-26T10:05:05.473Z",
          "FieldDataType": {
            "Name": "UUID"
          }
        },
        {
          "Id": "12940d03-fdaf-4e36-9a4c-b3ff6315fdf4",
          "Name": "CreatedBy",
          "IsPrimaryKey": false,
          "IsForeignKey": true,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceName": "fk_CreatedBy_4a49b3d5-48a8-48fc-92df-147c425be3f3",
          "ReferenceEntity": {
            "Name": "SystemUser",
            "DisplayName": "System Users",
            "EntityTypeId": 3,
            "EntityType": "SystemEntity",
            "FolderId": "00000000-0000-0000-0000-000000000000",
            "IsRbacEnabled": false,
            "IsInsightsEnabled": false,
            "InvalidIdentifiers": [],
            "IsModelReserved": false,
            "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
          },
          "ReferenceField": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Definition": {
              "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
              "Name": "Name",
              "IsPrimaryKey": false,
              "IsForeignKey": false,
              "IsExternalField": false,
              "IsHiddenField": false,
              "FieldCategoryId": 0,
              "IsUnique": false,
              "ReferenceType": "ManyToOne",
              "IsRequired": false,
              "IsEncrypted": false,
              "DisplayName": "Name",
              "IsSystemField": false,
              "IsAttachment": false,
              "IsRbacEnabled": false,
              "IsModelReserved": false,
              "CreatedTime": "2026-06-25T15:37:04.953Z",
              "UpdatedTime": "2026-06-25T15:37:04.953Z",
              "FieldDataType": {
                "Name": "NVARCHAR",
                "LengthLimit": 512
              }
            }
          },
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreatedBy",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "FieldDisplayType": "Relationship",
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:05:05.473Z",
          "UpdatedTime": "2026-06-26T10:05:05.473Z",
          "FieldDataType": {
            "Name": "RELATIONSHIP"
          }
        },
        {
          "Id": "5da2f46c-7cd2-4782-8542-decaeb0d5549",
          "Name": "UpdatedBy",
          "IsPrimaryKey": false,
          "IsForeignKey": true,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceName": "fk_UpdatedBy_dc63352f-4c8c-4d40-b0db-f308bed173ad",
          "ReferenceEntity": {
            "Name": "SystemUser",
            "DisplayName": "System Users",
            "EntityTypeId": 3,
            "EntityType": "SystemEntity",
            "FolderId": "00000000-0000-0000-0000-000000000000",
            "IsRbacEnabled": false,
            "IsInsightsEnabled": false,
            "InvalidIdentifiers": [],
            "IsModelReserved": false,
            "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
          },
          "ReferenceField": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Definition": {
              "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
              "Name": "Name",
              "IsPrimaryKey": false,
              "IsForeignKey": false,
              "IsExternalField": false,
              "IsHiddenField": false,
              "FieldCategoryId": 0,
              "IsUnique": false,
              "ReferenceType": "ManyToOne",
              "IsRequired": false,
              "IsEncrypted": false,
              "DisplayName": "Name",
              "IsSystemField": false,
              "IsAttachment": false,
              "IsRbacEnabled": false,
              "IsModelReserved": false,
              "CreatedTime": "2026-06-25T15:37:04.953Z",
              "UpdatedTime": "2026-06-25T15:37:04.953Z",
              "FieldDataType": {
                "Name": "NVARCHAR",
                "LengthLimit": 512
              }
            }
          },
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "UpdatedBy",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "FieldDisplayType": "Relationship",
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:05:05.473Z",
          "UpdatedTime": "2026-06-26T10:05:05.473Z",
          "FieldDataType": {
            "Name": "RELATIONSHIP"
          }
        }
      ],
      "RecordCount": 1,
      "StorageSizeInMB": 0.140625,
      "UsedStorageSizeInMB": 0.03125,
      "IsRbacEnabled": false,
      "IsInsightsEnabled": false,
      "InvalidIdentifiers": [],
      "IsModelReserved": false,
      "Id": "8fa39b80-4671-f111-ac9a-002248a16d28",
      "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "CreatedTime": "2026-06-26T10:05:05.45Z",
      "UpdatedTime": "2026-06-26T10:05:05.59Z"
    },
    {
      "Name": "ServiceRecoveryAuditBundleV2",
      "DisplayName": "Service Recovery Audit Bundle V2",
      "EntityTypeId": 0,
      "EntityType": "Entity",
      "Description": "Stores one governed service-recovery audit bundle using PascalCase fields verified for UiPath Data Fabric JSON insert/query readback.",
      "FolderId": "00000000-0000-0000-0000-000000000000",
      "Fields": [
        {
          "Id": "3fe8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "CaseId",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CaseId",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.263Z",
          "UpdatedTime": "2026-06-26T10:07:05.263Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "40e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "ServiceId",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "ServiceId",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.273Z",
          "UpdatedTime": "2026-06-26T10:07:05.273Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "41e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "ScenarioId",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "ScenarioId",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.393Z",
          "UpdatedTime": "2026-06-26T10:07:05.393Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 20
          }
        },
        {
          "Id": "42e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "AuditContractVersion",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "AuditContractVersion",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.407Z",
          "UpdatedTime": "2026-06-26T10:07:05.407Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "43e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "BusinessState",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "BusinessState",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.417Z",
          "UpdatedTime": "2026-06-26T10:07:05.417Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 50
          }
        },
        {
          "Id": "44e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "DerivedEvidenceState",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "DerivedEvidenceState",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.43Z",
          "UpdatedTime": "2026-06-26T10:07:05.43Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "45e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "ClosureBlockReason",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "ClosureBlockReason",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.44Z",
          "UpdatedTime": "2026-06-26T10:07:05.44Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "46e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "InterpretationPolicyVersion",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "InterpretationPolicyVersion",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.453Z",
          "UpdatedTime": "2026-06-26T10:07:05.453Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "47e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "DecisionPolicyVersion",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "DecisionPolicyVersion",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.467Z",
          "UpdatedTime": "2026-06-26T10:07:05.467Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "48e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "SourceCaseInstanceKey",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "SourceCaseInstanceKey",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.477Z",
          "UpdatedTime": "2026-06-26T10:07:05.477Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 100
          }
        },
        {
          "Id": "49e8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "SourceTaskId",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "SourceTaskId",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.487Z",
          "UpdatedTime": "2026-06-26T10:07:05.487Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 50
          }
        },
        {
          "Id": "4ae8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "PackageVersion",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "PackageVersion",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.5Z",
          "UpdatedTime": "2026-06-26T10:07:05.5Z",
          "FieldDataType": {
            "Name": "STRING",
            "LengthLimit": 50
          }
        },
        {
          "Id": "4be8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "RawAgentEventJson",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "RawAgentEventJson",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.513Z",
          "UpdatedTime": "2026-06-26T10:07:05.513Z",
          "FieldDataType": {
            "Name": "MULTILINE_TEXT",
            "LengthLimit": 10000
          }
        },
        {
          "Id": "4ce8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "PolicyDecisionEventJson",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "PolicyDecisionEventJson",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.523Z",
          "UpdatedTime": "2026-06-26T10:07:05.523Z",
          "FieldDataType": {
            "Name": "MULTILINE_TEXT",
            "LengthLimit": 10000
          }
        },
        {
          "Id": "4de8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "ReviewerPacketJson",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "ReviewerPacketJson",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.537Z",
          "UpdatedTime": "2026-06-26T10:07:05.537Z",
          "FieldDataType": {
            "Name": "MULTILINE_TEXT",
            "LengthLimit": 10000
          }
        },
        {
          "Id": "4ee8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "AuditBundleJson",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "AuditBundleJson",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.547Z",
          "UpdatedTime": "2026-06-26T10:07:05.547Z",
          "FieldDataType": {
            "Name": "MULTILINE_TEXT",
            "LengthLimit": 10000
          }
        },
        {
          "Id": "4fe8f6c7-4671-f111-ac9a-002248a16d28",
          "Name": "CreatedAt",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreatedAt",
          "Description": "",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": false,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.563Z",
          "UpdatedTime": "2026-06-26T10:07:05.563Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ",
            "LengthLimit": 1000
          }
        },
        {
          "Id": "4b0b67d0-55d8-442a-bf25-0eb8f081cd31",
          "Name": "UpdatedBy",
          "IsPrimaryKey": false,
          "IsForeignKey": true,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceName": "fk_UpdatedBy_0f94c174-fff1-4c02-a979-c74873335179",
          "ReferenceEntity": {
            "Name": "SystemUser",
            "DisplayName": "System Users",
            "EntityTypeId": 3,
            "EntityType": "SystemEntity",
            "FolderId": "00000000-0000-0000-0000-000000000000",
            "IsRbacEnabled": false,
            "IsInsightsEnabled": false,
            "InvalidIdentifiers": [],
            "IsModelReserved": false,
            "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
          },
          "ReferenceField": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Definition": {
              "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
              "Name": "Name",
              "IsPrimaryKey": false,
              "IsForeignKey": false,
              "IsExternalField": false,
              "IsHiddenField": false,
              "FieldCategoryId": 0,
              "IsUnique": false,
              "ReferenceType": "ManyToOne",
              "IsRequired": false,
              "IsEncrypted": false,
              "DisplayName": "Name",
              "IsSystemField": false,
              "IsAttachment": false,
              "IsRbacEnabled": false,
              "IsModelReserved": false,
              "CreatedTime": "2026-06-25T15:37:04.953Z",
              "UpdatedTime": "2026-06-25T15:37:04.953Z",
              "FieldDataType": {
                "Name": "NVARCHAR",
                "LengthLimit": 512
              }
            }
          },
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "UpdatedBy",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "FieldDisplayType": "Relationship",
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.187Z",
          "UpdatedTime": "2026-06-26T10:07:05.187Z",
          "FieldDataType": {
            "Name": "RELATIONSHIP"
          }
        },
        {
          "Id": "9b49d6f7-82b4-4b8e-9f2f-1c6120fea5a9",
          "Name": "CreateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.187Z",
          "UpdatedTime": "2026-06-26T10:07:05.187Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        },
        {
          "Id": "4c8d9f5b-e132-4429-8e53-20d3ff479a82",
          "Name": "CreatedBy",
          "IsPrimaryKey": false,
          "IsForeignKey": true,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceName": "fk_CreatedBy_aaa13563-2292-4640-9b13-45835d0b9861",
          "ReferenceEntity": {
            "Name": "SystemUser",
            "DisplayName": "System Users",
            "EntityTypeId": 3,
            "EntityType": "SystemEntity",
            "FolderId": "00000000-0000-0000-0000-000000000000",
            "IsRbacEnabled": false,
            "IsInsightsEnabled": false,
            "InvalidIdentifiers": [],
            "IsModelReserved": false,
            "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
          },
          "ReferenceField": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Definition": {
              "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
              "Name": "Name",
              "IsPrimaryKey": false,
              "IsForeignKey": false,
              "IsExternalField": false,
              "IsHiddenField": false,
              "FieldCategoryId": 0,
              "IsUnique": false,
              "ReferenceType": "ManyToOne",
              "IsRequired": false,
              "IsEncrypted": false,
              "DisplayName": "Name",
              "IsSystemField": false,
              "IsAttachment": false,
              "IsRbacEnabled": false,
              "IsModelReserved": false,
              "CreatedTime": "2026-06-25T15:37:04.953Z",
              "UpdatedTime": "2026-06-25T15:37:04.953Z",
              "FieldDataType": {
                "Name": "NVARCHAR",
                "LengthLimit": 512
              }
            }
          },
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "CreatedBy",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "FieldDisplayType": "Relationship",
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.187Z",
          "UpdatedTime": "2026-06-26T10:07:05.187Z",
          "FieldDataType": {
            "Name": "RELATIONSHIP"
          }
        },
        {
          "Id": "6f74b9de-ebc0-4b85-8595-5c79b5ce8a68",
          "Name": "UpdateTime",
          "IsPrimaryKey": false,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": false,
          "IsEncrypted": false,
          "DisplayName": "UpdateTime",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.187Z",
          "UpdatedTime": "2026-06-26T10:07:05.187Z",
          "FieldDataType": {
            "Name": "DATETIME_WITH_TZ"
          }
        },
        {
          "Id": "51286e12-c61d-4388-a7ba-ac8038542818",
          "Name": "Id",
          "IsPrimaryKey": true,
          "IsForeignKey": false,
          "IsExternalField": false,
          "IsHiddenField": false,
          "FieldCategoryId": 0,
          "IsUnique": false,
          "ReferenceType": "ManyToOne",
          "IsRequired": true,
          "IsEncrypted": false,
          "DisplayName": "Id",
          "Description": "System built-in field",
          "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
          "IsSystemField": true,
          "IsAttachment": false,
          "IsRbacEnabled": false,
          "IsModelReserved": false,
          "CreatedTime": "2026-06-26T10:07:05.187Z",
          "UpdatedTime": "2026-06-26T10:07:05.187Z",
          "FieldDataType": {
            "Name": "UUID"
          }
        }
      ],
      "RecordCount": 1,
      "StorageSizeInMB": 0.210937,
      "UsedStorageSizeInMB": 0.054687,
      "IsRbacEnabled": false,
      "IsInsightsEnabled": false,
      "InvalidIdentifiers": [],
      "IsModelReserved": false,
      "Id": "35e8f6c7-4671-f111-ac9a-002248a16d28",
      "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
      "CreatedTime": "2026-06-26T10:07:05.167Z",
      "UpdatedTime": "2026-06-26T10:07:05.563Z"
    }
  ]
}

(exit 0)
```

## `uip df entities get 328ef8b6-ab70-f111-ac9a-002248a16d28 --output json`

```text
{
  "Result": "Success",
  "Code": "EntitySchema",
  "Data": {
    "Name": "ServiceRecoveryAuditBundle",
    "DisplayName": "Service Recovery Audit Bundle",
    "EntityTypeId": 0,
    "EntityType": "Entity",
    "Description": "Stores one governed service-recovery audit bundle for UiPath Maestro Case validation and demo reconstruction.",
    "FolderId": "00000000-0000-0000-0000-000000000000",
    "Fields": [
      {
        "Id": "3c8ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "case_id",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "case_id",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.143Z",
        "UpdatedTime": "2026-06-25T15:37:05.143Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "3d8ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "service_id",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "service_id",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.157Z",
        "UpdatedTime": "2026-06-25T15:37:05.157Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "3e8ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "scenario_id",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "scenario_id",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.17Z",
        "UpdatedTime": "2026-06-25T15:37:05.17Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 20
        }
      },
      {
        "Id": "3f8ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "audit_contract_version",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "audit_contract_version",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.183Z",
        "UpdatedTime": "2026-06-25T15:37:05.183Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "408ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "business_state",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "business_state",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.193Z",
        "UpdatedTime": "2026-06-25T15:37:05.193Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 50
        }
      },
      {
        "Id": "418ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "derived_evidence_state",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "derived_evidence_state",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.203Z",
        "UpdatedTime": "2026-06-25T15:37:05.203Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "428ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "closure_block_reason",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "closure_block_reason",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.213Z",
        "UpdatedTime": "2026-06-25T15:37:05.213Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "438ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "interpretation_policy_version",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "interpretation_policy_version",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.227Z",
        "UpdatedTime": "2026-06-25T15:37:05.227Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "448ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "decision_policy_version",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "decision_policy_version",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.237Z",
        "UpdatedTime": "2026-06-25T15:37:05.237Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "458ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "source_case_instance_key",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "source_case_instance_key",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.25Z",
        "UpdatedTime": "2026-06-25T15:37:05.25Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "468ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "source_task_id",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "source_task_id",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.26Z",
        "UpdatedTime": "2026-06-25T15:37:05.26Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 50
        }
      },
      {
        "Id": "478ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "package_version",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "package_version",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.27Z",
        "UpdatedTime": "2026-06-25T15:37:05.27Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 50
        }
      },
      {
        "Id": "488ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "raw_agent_event_json",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "raw_agent_event_json",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.283Z",
        "UpdatedTime": "2026-06-25T15:37:05.283Z",
        "FieldDataType": {
          "Name": "MULTILINE_TEXT",
          "LengthLimit": 10000
        }
      },
      {
        "Id": "498ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "policy_decision_event_json",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "policy_decision_event_json",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.307Z",
        "UpdatedTime": "2026-06-25T15:37:05.307Z",
        "FieldDataType": {
          "Name": "MULTILINE_TEXT",
          "LengthLimit": 10000
        }
      },
      {
        "Id": "4a8ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "reviewer_packet_json",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "reviewer_packet_json",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.32Z",
        "UpdatedTime": "2026-06-25T15:37:05.32Z",
        "FieldDataType": {
          "Name": "MULTILINE_TEXT",
          "LengthLimit": 10000
        }
      },
      {
        "Id": "4b8ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "audit_bundle_json",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "audit_bundle_json",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.333Z",
        "UpdatedTime": "2026-06-25T15:37:05.333Z",
        "FieldDataType": {
          "Name": "MULTILINE_TEXT",
          "LengthLimit": 10000
        }
      },
      {
        "Id": "4c8ef8b6-ab70-f111-ac9a-002248a16d28",
        "Name": "created_at",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "created_at",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.343Z",
        "UpdatedTime": "2026-06-25T15:37:05.343Z",
        "FieldDataType": {
          "Name": "DATETIME_WITH_TZ",
          "LengthLimit": 1000
        }
      },
      {
        "Id": "29f20c20-e041-4dd4-b3c9-6a33cf42fbbc",
        "Name": "RecordOwner",
        "IsPrimaryKey": false,
        "IsForeignKey": true,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceName": "fk_RecordOwner_87bee513-08ac-4fc3-a375-43f953f964b9",
        "ReferenceEntity": {
          "Name": "SystemUser",
          "DisplayName": "System Users",
          "EntityTypeId": 3,
          "EntityType": "SystemEntity",
          "FolderId": "00000000-0000-0000-0000-000000000000",
          "IsRbacEnabled": false,
          "IsInsightsEnabled": false,
          "InvalidIdentifiers": [],
          "IsModelReserved": false,
          "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
        },
        "ReferenceField": {
          "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
          "Definition": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Name": "Name",
            "IsPrimaryKey": false,
            "IsForeignKey": false,
            "IsExternalField": false,
            "IsHiddenField": false,
            "FieldCategoryId": 0,
            "IsUnique": false,
            "ReferenceType": "ManyToOne",
            "IsRequired": false,
            "IsEncrypted": false,
            "DisplayName": "Name",
            "IsSystemField": false,
            "IsAttachment": false,
            "IsRbacEnabled": false,
            "IsModelReserved": false,
            "CreatedTime": "2026-06-25T15:37:04.953Z",
            "UpdatedTime": "2026-06-25T15:37:04.953Z",
            "FieldDataType": {
              "Name": "NVARCHAR",
              "LengthLimit": 512
            }
          }
        },
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "RecordOwner",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "FieldDisplayType": "Relationship",
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.07Z",
        "UpdatedTime": "2026-06-25T15:37:05.07Z",
        "FieldDataType": {
          "Name": "RELATIONSHIP"
        }
      },
      {
        "Id": "b1ca5bad-a8ff-486b-854f-7eefa61a8f51",
        "Name": "Id",
        "IsPrimaryKey": true,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "Id",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.07Z",
        "UpdatedTime": "2026-06-25T15:37:05.07Z",
        "FieldDataType": {
          "Name": "UUID"
        }
      },
      {
        "Id": "0fb8b9e4-8eed-4b84-acc6-98cac21e7df3",
        "Name": "UpdateTime",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "UpdateTime",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.07Z",
        "UpdatedTime": "2026-06-25T15:37:05.07Z",
        "FieldDataType": {
          "Name": "DATETIME_WITH_TZ"
        }
      },
      {
        "Id": "e82195c2-76ec-4ada-a539-afc98913d012",
        "Name": "CreateTime",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "CreateTime",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.07Z",
        "UpdatedTime": "2026-06-25T15:37:05.07Z",
        "FieldDataType": {
          "Name": "DATETIME_WITH_TZ"
        }
      },
      {
        "Id": "8b27783e-fdd2-463f-8941-cb21985f56cc",
        "Name": "UpdatedBy",
        "IsPrimaryKey": false,
        "IsForeignKey": true,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceName": "fk_UpdatedBy_55331d30-1048-4517-8841-a0d600092302",
        "ReferenceEntity": {
          "Name": "SystemUser",
          "DisplayName": "System Users",
          "EntityTypeId": 3,
          "EntityType": "SystemEntity",
          "FolderId": "00000000-0000-0000-0000-000000000000",
          "IsRbacEnabled": false,
          "IsInsightsEnabled": false,
          "InvalidIdentifiers": [],
          "IsModelReserved": false,
          "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
        },
        "ReferenceField": {
          "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
          "Definition": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Name": "Name",
            "IsPrimaryKey": false,
            "IsForeignKey": false,
            "IsExternalField": false,
            "IsHiddenField": false,
            "FieldCategoryId": 0,
            "IsUnique": false,
            "ReferenceType": "ManyToOne",
            "IsRequired": false,
            "IsEncrypted": false,
            "DisplayName": "Name",
            "IsSystemField": false,
            "IsAttachment": false,
            "IsRbacEnabled": false,
            "IsModelReserved": false,
            "CreatedTime": "2026-06-25T15:37:04.953Z",
            "UpdatedTime": "2026-06-25T15:37:04.953Z",
            "FieldDataType": {
              "Name": "NVARCHAR",
              "LengthLimit": 512
            }
          }
        },
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "UpdatedBy",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "FieldDisplayType": "Relationship",
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.07Z",
        "UpdatedTime": "2026-06-25T15:37:05.07Z",
        "FieldDataType": {
          "Name": "RELATIONSHIP"
        }
      },
      {
        "Id": "3b33ee30-0542-42bb-a4b6-f1f18f2b1fb7",
        "Name": "CreatedBy",
        "IsPrimaryKey": false,
        "IsForeignKey": true,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceName": "fk_CreatedBy_5b269828-016f-4902-aa02-b11b8a456121",
        "ReferenceEntity": {
          "Name": "SystemUser",
          "DisplayName": "System Users",
          "EntityTypeId": 3,
          "EntityType": "SystemEntity",
          "FolderId": "00000000-0000-0000-0000-000000000000",
          "IsRbacEnabled": false,
          "IsInsightsEnabled": false,
          "InvalidIdentifiers": [],
          "IsModelReserved": false,
          "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
        },
        "ReferenceField": {
          "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
          "Definition": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Name": "Name",
            "IsPrimaryKey": false,
            "IsForeignKey": false,
            "IsExternalField": false,
            "IsHiddenField": false,
            "FieldCategoryId": 0,
            "IsUnique": false,
            "ReferenceType": "ManyToOne",
            "IsRequired": false,
            "IsEncrypted": false,
            "DisplayName": "Name",
            "IsSystemField": false,
            "IsAttachment": false,
            "IsRbacEnabled": false,
            "IsModelReserved": false,
            "CreatedTime": "2026-06-25T15:37:04.953Z",
            "UpdatedTime": "2026-06-25T15:37:04.953Z",
            "FieldDataType": {
              "Name": "NVARCHAR",
              "LengthLimit": 512
            }
          }
        },
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "CreatedBy",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "FieldDisplayType": "Relationship",
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-25T15:37:05.07Z",
        "UpdatedTime": "2026-06-25T15:37:05.07Z",
        "FieldDataType": {
          "Name": "RELATIONSHIP"
        }
      }
    ],
    "IsRbacEnabled": false,
    "IsInsightsEnabled": false,
    "InvalidIdentifiers": [],
    "IsModelReserved": false,
    "Id": "328ef8b6-ab70-f111-ac9a-002248a16d28",
    "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
    "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
    "CreatedTime": "2026-06-25T15:37:05.057Z",
    "UpdatedTime": "2026-06-25T15:37:05.343Z"
  }
}

(exit 0)
```

## `uip df entities get 35e8f6c7-4671-f111-ac9a-002248a16d28 --output json`

```text
{
  "Result": "Success",
  "Code": "EntitySchema",
  "Data": {
    "Name": "ServiceRecoveryAuditBundleV2",
    "DisplayName": "Service Recovery Audit Bundle V2",
    "EntityTypeId": 0,
    "EntityType": "Entity",
    "Description": "Stores one governed service-recovery audit bundle using PascalCase fields verified for UiPath Data Fabric JSON insert/query readback.",
    "FolderId": "00000000-0000-0000-0000-000000000000",
    "Fields": [
      {
        "Id": "3fe8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "CaseId",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "CaseId",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.263Z",
        "UpdatedTime": "2026-06-26T10:07:05.263Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "40e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "ServiceId",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "ServiceId",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.273Z",
        "UpdatedTime": "2026-06-26T10:07:05.273Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "41e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "ScenarioId",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "ScenarioId",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.393Z",
        "UpdatedTime": "2026-06-26T10:07:05.393Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 20
        }
      },
      {
        "Id": "42e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "AuditContractVersion",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "AuditContractVersion",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.407Z",
        "UpdatedTime": "2026-06-26T10:07:05.407Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "43e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "BusinessState",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "BusinessState",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.417Z",
        "UpdatedTime": "2026-06-26T10:07:05.417Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 50
        }
      },
      {
        "Id": "44e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "DerivedEvidenceState",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "DerivedEvidenceState",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.43Z",
        "UpdatedTime": "2026-06-26T10:07:05.43Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "45e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "ClosureBlockReason",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "ClosureBlockReason",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.44Z",
        "UpdatedTime": "2026-06-26T10:07:05.44Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "46e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "InterpretationPolicyVersion",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "InterpretationPolicyVersion",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.453Z",
        "UpdatedTime": "2026-06-26T10:07:05.453Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "47e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "DecisionPolicyVersion",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "DecisionPolicyVersion",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.467Z",
        "UpdatedTime": "2026-06-26T10:07:05.467Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "48e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "SourceCaseInstanceKey",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "SourceCaseInstanceKey",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.477Z",
        "UpdatedTime": "2026-06-26T10:07:05.477Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 100
        }
      },
      {
        "Id": "49e8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "SourceTaskId",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "SourceTaskId",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.487Z",
        "UpdatedTime": "2026-06-26T10:07:05.487Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 50
        }
      },
      {
        "Id": "4ae8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "PackageVersion",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "PackageVersion",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.5Z",
        "UpdatedTime": "2026-06-26T10:07:05.5Z",
        "FieldDataType": {
          "Name": "STRING",
          "LengthLimit": 50
        }
      },
      {
        "Id": "4be8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "RawAgentEventJson",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "RawAgentEventJson",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.513Z",
        "UpdatedTime": "2026-06-26T10:07:05.513Z",
        "FieldDataType": {
          "Name": "MULTILINE_TEXT",
          "LengthLimit": 10000
        }
      },
      {
        "Id": "4ce8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "PolicyDecisionEventJson",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "PolicyDecisionEventJson",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.523Z",
        "UpdatedTime": "2026-06-26T10:07:05.523Z",
        "FieldDataType": {
          "Name": "MULTILINE_TEXT",
          "LengthLimit": 10000
        }
      },
      {
        "Id": "4de8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "ReviewerPacketJson",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "ReviewerPacketJson",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.537Z",
        "UpdatedTime": "2026-06-26T10:07:05.537Z",
        "FieldDataType": {
          "Name": "MULTILINE_TEXT",
          "LengthLimit": 10000
        }
      },
      {
        "Id": "4ee8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "AuditBundleJson",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "AuditBundleJson",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.547Z",
        "UpdatedTime": "2026-06-26T10:07:05.547Z",
        "FieldDataType": {
          "Name": "MULTILINE_TEXT",
          "LengthLimit": 10000
        }
      },
      {
        "Id": "4fe8f6c7-4671-f111-ac9a-002248a16d28",
        "Name": "CreatedAt",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "CreatedAt",
        "Description": "",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": false,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.563Z",
        "UpdatedTime": "2026-06-26T10:07:05.563Z",
        "FieldDataType": {
          "Name": "DATETIME_WITH_TZ",
          "LengthLimit": 1000
        }
      },
      {
        "Id": "4b0b67d0-55d8-442a-bf25-0eb8f081cd31",
        "Name": "UpdatedBy",
        "IsPrimaryKey": false,
        "IsForeignKey": true,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceName": "fk_UpdatedBy_0f94c174-fff1-4c02-a979-c74873335179",
        "ReferenceEntity": {
          "Name": "SystemUser",
          "DisplayName": "System Users",
          "EntityTypeId": 3,
          "EntityType": "SystemEntity",
          "FolderId": "00000000-0000-0000-0000-000000000000",
          "IsRbacEnabled": false,
          "IsInsightsEnabled": false,
          "InvalidIdentifiers": [],
          "IsModelReserved": false,
          "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
        },
        "ReferenceField": {
          "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
          "Definition": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Name": "Name",
            "IsPrimaryKey": false,
            "IsForeignKey": false,
            "IsExternalField": false,
            "IsHiddenField": false,
            "FieldCategoryId": 0,
            "IsUnique": false,
            "ReferenceType": "ManyToOne",
            "IsRequired": false,
            "IsEncrypted": false,
            "DisplayName": "Name",
            "IsSystemField": false,
            "IsAttachment": false,
            "IsRbacEnabled": false,
            "IsModelReserved": false,
            "CreatedTime": "2026-06-25T15:37:04.953Z",
            "UpdatedTime": "2026-06-25T15:37:04.953Z",
            "FieldDataType": {
              "Name": "NVARCHAR",
              "LengthLimit": 512
            }
          }
        },
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "UpdatedBy",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "FieldDisplayType": "Relationship",
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.187Z",
        "UpdatedTime": "2026-06-26T10:07:05.187Z",
        "FieldDataType": {
          "Name": "RELATIONSHIP"
        }
      },
      {
        "Id": "52004bd0-abd1-4da1-8409-1315c967b7ec",
        "Name": "RecordOwner",
        "IsPrimaryKey": false,
        "IsForeignKey": true,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceName": "fk_RecordOwner_5be66b10-954d-45fb-b748-b2cc61560b5c",
        "ReferenceEntity": {
          "Name": "SystemUser",
          "DisplayName": "System Users",
          "EntityTypeId": 3,
          "EntityType": "SystemEntity",
          "FolderId": "00000000-0000-0000-0000-000000000000",
          "IsRbacEnabled": false,
          "IsInsightsEnabled": false,
          "InvalidIdentifiers": [],
          "IsModelReserved": false,
          "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
        },
        "ReferenceField": {
          "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
          "Definition": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Name": "Name",
            "IsPrimaryKey": false,
            "IsForeignKey": false,
            "IsExternalField": false,
            "IsHiddenField": false,
            "FieldCategoryId": 0,
            "IsUnique": false,
            "ReferenceType": "ManyToOne",
            "IsRequired": false,
            "IsEncrypted": false,
            "DisplayName": "Name",
            "IsSystemField": false,
            "IsAttachment": false,
            "IsRbacEnabled": false,
            "IsModelReserved": false,
            "CreatedTime": "2026-06-25T15:37:04.953Z",
            "UpdatedTime": "2026-06-25T15:37:04.953Z",
            "FieldDataType": {
              "Name": "NVARCHAR",
              "LengthLimit": 512
            }
          }
        },
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "RecordOwner",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "FieldDisplayType": "Relationship",
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.187Z",
        "UpdatedTime": "2026-06-26T10:07:05.187Z",
        "FieldDataType": {
          "Name": "RELATIONSHIP"
        }
      },
      {
        "Id": "9b49d6f7-82b4-4b8e-9f2f-1c6120fea5a9",
        "Name": "CreateTime",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "CreateTime",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.187Z",
        "UpdatedTime": "2026-06-26T10:07:05.187Z",
        "FieldDataType": {
          "Name": "DATETIME_WITH_TZ"
        }
      },
      {
        "Id": "4c8d9f5b-e132-4429-8e53-20d3ff479a82",
        "Name": "CreatedBy",
        "IsPrimaryKey": false,
        "IsForeignKey": true,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceName": "fk_CreatedBy_aaa13563-2292-4640-9b13-45835d0b9861",
        "ReferenceEntity": {
          "Name": "SystemUser",
          "DisplayName": "System Users",
          "EntityTypeId": 3,
          "EntityType": "SystemEntity",
          "FolderId": "00000000-0000-0000-0000-000000000000",
          "IsRbacEnabled": false,
          "IsInsightsEnabled": false,
          "InvalidIdentifiers": [],
          "IsModelReserved": false,
          "Id": "2a8ef8b6-ab70-f111-ac9a-002248a16d28"
        },
        "ReferenceField": {
          "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
          "Definition": {
            "Id": "384e2412-cd07-4718-81f5-2440acefac7e",
            "Name": "Name",
            "IsPrimaryKey": false,
            "IsForeignKey": false,
            "IsExternalField": false,
            "IsHiddenField": false,
            "FieldCategoryId": 0,
            "IsUnique": false,
            "ReferenceType": "ManyToOne",
            "IsRequired": false,
            "IsEncrypted": false,
            "DisplayName": "Name",
            "IsSystemField": false,
            "IsAttachment": false,
            "IsRbacEnabled": false,
            "IsModelReserved": false,
            "CreatedTime": "2026-06-25T15:37:04.953Z",
            "UpdatedTime": "2026-06-25T15:37:04.953Z",
            "FieldDataType": {
              "Name": "NVARCHAR",
              "LengthLimit": 512
            }
          }
        },
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "CreatedBy",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "FieldDisplayType": "Relationship",
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.187Z",
        "UpdatedTime": "2026-06-26T10:07:05.187Z",
        "FieldDataType": {
          "Name": "RELATIONSHIP"
        }
      },
      {
        "Id": "6f74b9de-ebc0-4b85-8595-5c79b5ce8a68",
        "Name": "UpdateTime",
        "IsPrimaryKey": false,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": false,
        "IsEncrypted": false,
        "DisplayName": "UpdateTime",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.187Z",
        "UpdatedTime": "2026-06-26T10:07:05.187Z",
        "FieldDataType": {
          "Name": "DATETIME_WITH_TZ"
        }
      },
      {
        "Id": "51286e12-c61d-4388-a7ba-ac8038542818",
        "Name": "Id",
        "IsPrimaryKey": true,
        "IsForeignKey": false,
        "IsExternalField": false,
        "IsHiddenField": false,
        "FieldCategoryId": 0,
        "IsUnique": false,
        "ReferenceType": "ManyToOne",
        "IsRequired": true,
        "IsEncrypted": false,
        "DisplayName": "Id",
        "Description": "System built-in field",
        "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
        "IsSystemField": true,
        "IsAttachment": false,
        "IsRbacEnabled": false,
        "IsModelReserved": false,
        "CreatedTime": "2026-06-26T10:07:05.187Z",
        "UpdatedTime": "2026-06-26T10:07:05.187Z",
        "FieldDataType": {
          "Name": "UUID"
        }
      }
    ],
    "IsRbacEnabled": false,
    "IsInsightsEnabled": false,
    "InvalidIdentifiers": [],
    "IsModelReserved": false,
    "Id": "35e8f6c7-4671-f111-ac9a-002248a16d28",
    "CreatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
    "UpdatedBy": "f5e77dba-8b15-4103-8605-dc11685dd53e",
    "CreatedTime": "2026-06-26T10:07:05.167Z",
    "UpdatedTime": "2026-06-26T10:07:05.563Z"
  }
}

(exit 0)
```

## `uip df records get 328ef8b6-ab70-f111-ac9a-002248a16d28 DA42769C-33B7-4701-A266-019F032AF376 --output json`

```text
{
  "Result": "Success",
  "Code": "RecordDetails",
  "Data": {
    "RecordOwner": "F5E77DBA-8B15-4103-8605-DC11685DD53E",
    "Id": "DA42769C-33B7-4701-A266-019F032AF376",
    "UpdateTime": "2026-06-26T09:59:14.1061719+00:00",
    "CreateTime": "2026-06-26T09:02:54.3218278+00:00",
    "UpdatedBy": "F5E77DBA-8B15-4103-8605-DC11685DD53E",
    "CreatedBy": "F5E77DBA-8B15-4103-8605-DC11685DD53E"
  }
}

(exit 0)
```

## `uip df records query 328ef8b6-ab70-f111-ac9a-002248a16d28 --body {"selectedFields":["Id","case_id","scenario_id","service_id","business_state","derived_evidence_state","closure_block_reason","interpretation_policy_version","decision_policy_version","source_case_instance_key","source_task_id","package_version"]} --limit 5 --output json`

```text
{
  "Result": "Success",
  "Code": "RecordQuery",
  "Data": {
    "Items": [
      {
        "Id": "2C714242-46D0-4ECE-9361-019F031FC9F3"
      },
      {
        "Id": "3B4974CE-54C5-40BF-B52E-019F03200688"
      },
      {
        "Id": "06918198-C357-485D-BE75-019F03200BF9"
      },
      {
        "Id": "B1111404-00B5-49A7-8C5E-019F03201151"
      },
      {
        "Id": "D75152E7-B59A-48ED-B02F-019F032016EC"
      }
    ],
    "TotalCount": 30,
    "HasNextPage": true,
    "NextCursor": {
      "Value": "eyJ0eXBlIjoib2Zmc2V0IiwicGFnZVNpemUiOjUsInBhZ2VOdW1iZXIiOjJ9"
    },
    "CurrentPage": 1,
    "TotalPages": 6,
    "SupportsPageJump": true
  }
}

(exit 0)
```

## `uip df records get 35e8f6c7-4671-f111-ac9a-002248a16d28 F9D838CE-4671-F111-AC9A-0022489A9A06 --output json`

```text
{
  "Result": "Success",
  "Code": "RecordDetails",
  "Data": {
    "CaseId": "CASE-BG-CONTRA",
    "ServiceId": "SVC-BG-1",
    "ScenarioId": "E-004",
    "AuditContractVersion": "service-recovery-audit-v1",
    "BusinessState": "green",
    "DerivedEvidenceState": "contradicting",
    "ClosureBlockReason": "source_contradiction",
    "InterpretationPolicyVersion": "ip-v1",
    "DecisionPolicyVersion": "dp-v1",
    "SourceCaseInstanceKey": "9fc6fece-55ed-4fb2-b11a-6c96f7a3314e",
    "SourceTaskId": "4328396",
    "PackageVersion": "1.0.6",
    "RawAgentEventJson": "{\"adversarial_interpretation\":null,\"case_id\":\"CASE-BG-CONTRA\",\"confidence\":0.82,\"customer_impact_summary\":null,\"event_id\":\"AIE-E004\",\"event_type\":\"AgentInterpretationEvent\",\"evidence_gaps\":[],\"failure_category\":\"activation_failure\",\"interpretation_policy_version\":\"ip-v1\",\"operator_note\":null,\"rationale\":\"Business systems look complete, so the agent recommends closure pending policy review.\",\"recommended_actions\":[],\"recommended_next_stage\":\"closure_candidate\",\"reviewer_questions\":[],\"urgency\":null}",
    "PolicyDecisionEventJson": "{\"allowed_actions\":[\"human_review\",\"request_evidence\",\"open_investigation\"],\"block_reason\":\"source_contradiction\",\"case_id\":\"CASE-BG-CONTRA\",\"decision\":\"require_human_review\",\"decision_policy_version\":\"dp-v1\",\"event_id\":\"PDE-E-004\",\"event_type\":\"PolicyDecisionEvent\",\"from_recommended_stage\":\"closure_candidate\",\"links_to\":\"AIE-E004\",\"reason_codes\":[\"source_contradiction\"],\"to_stage\":\"human_review\"}",
    "ReviewerPacketJson": "{\"block_reason\":\"source_contradiction\",\"content\":\"Service recovery exception review required: CRM/order/billing/support notes are green, but fresh authoritative telemetry contradicts the business state. Do not close; open human exception review.\",\"evidence_table\":[{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"crm_order_status\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:00:00Z\",\"source\":\"crm\",\"ttl_seconds\":86400,\"value\":\"active\"},{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"billing_status\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:01:00Z\",\"source\":\"billing\",\"ttl_seconds\":86400,\"value\":\"clear\"},{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"inventory_assignment\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:02:00Z\",\"source\":\"inventory\",\"ttl_seconds\":86400,\"value\":\"assigned_match\"},{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"service_live_status\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:03:00Z\",\"source\":\"network_telemetry\",\"ttl_seconds\":300,\"value\":\"not_live\"},{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"dispatch_status\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:04:00Z\",\"source\":\"dispatch\",\"ttl_seconds\":86400,\"value\":\"complete\"}],\"policy_decision\":{\"allowed_actions\":[\"human_review\",\"request_evidence\",\"open_investigation\"],\"block_reason\":\"source_contradiction\",\"case_id\":\"CASE-BG-CONTRA\",\"decision\":\"require_human_review\",\"decision_policy_version\":\"dp-v1\",\"event_id\":\"PDE-E-004\",\"event_type\":\"PolicyDecisionEvent\",\"from_recommended_stage\":\"closure_candidate\",\"links_to\":\"AIE-E004\",\"reason_codes\":[\"source_contradiction\"],\"to_stage\":\"human_review\"},\"raw_agent_recommendation\":{\"adversarial_interpretation\":null,\"case_id\":\"CASE-BG-CONTRA\",\"confidence\":0.82,\"customer_impact_summary\":null,\"event_id\":\"AIE-E004\",\"event_type\":\"AgentInterpretationEvent\",\"evidence_gaps\":[],\"failure_category\":\"activation_failure\",\"interpretation_policy_version\":\"ip-v1\",\"operator_note\":null,\"rationale\":\"Business systems look complete, so the agent recommends closure pending policy review.\",\"recommended_actions\":[],\"recommended_next_stage\":\"closure_candidate\",\"reviewer_questions\":[],\"urgency\":null},\"recommended_options\":[\"human_review\",\"request_evidence\",\"open_investigation\"],\"rendering_status\":\"structured_packet_ready\"}",
    "AuditBundleJson": "{\"agent_interpretation_event\":{\"adversarial_interpretation\":null,\"case_id\":\"CASE-BG-CONTRA\",\"confidence\":0.82,\"customer_impact_summary\":null,\"event_id\":\"AIE-E004\",\"event_type\":\"AgentInterpretationEvent\",\"evidence_gaps\":[],\"failure_category\":\"activation_failure\",\"interpretation_policy_version\":\"ip-v1\",\"operator_note\":null,\"rationale\":\"Business systems look complete, so the agent recommends closure pending policy review.\",\"recommended_actions\":[],\"recommended_next_stage\":\"closure_candidate\",\"reviewer_questions\":[],\"urgency\":null},\"audit_contract_version\":\"service-recovery-audit-v1\",\"case_id\":\"CASE-BG-CONTRA\",\"case_instance\":{\"case_process_auto_update\":null,\"case_process_package_key\":null,\"case_process_package_version\":null,\"case_stage\":\"intake\",\"severity\":\"normal\",\"sla_deadline\":\"2026-06-18T12:00:00Z\"},\"events\":[{\"business_state\":\"green\",\"case_id\":\"CASE-BG-CONTRA\",\"closure_block_reason\":\"source_contradiction\",\"derived_evidence_state\":\"contradicting\",\"event_id\":\"ESE-CASE-BG-CONTRA\",\"event_type\":\"EvidenceStateEvent\",\"evidence_signal_count\":5,\"sort_order\":10},{\"adversarial_interpretation\":null,\"case_id\":\"CASE-BG-CONTRA\",\"confidence\":0.82,\"customer_impact_summary\":null,\"event_id\":\"AIE-E004\",\"event_type\":\"AgentInterpretationEvent\",\"evidence_gaps\":[],\"failure_category\":\"activation_failure\",\"interpretation_policy_version\":\"ip-v1\",\"operator_note\":null,\"rationale\":\"Business systems look complete, so the agent recommends closure pending policy review.\",\"recommended_actions\":[],\"recommended_next_stage\":\"closure_candidate\",\"reviewer_questions\":[],\"sort_order\":20,\"urgency\":null},{\"allowed_actions\":[\"human_review\",\"request_evidence\",\"open_investigation\"],\"block_reason\":\"source_contradiction\",\"case_id\":\"CASE-BG-CONTRA\",\"decision\":\"require_human_review\",\"decision_policy_version\":\"dp-v1\",\"event_id\":\"PDE-E-004\",\"event_type\":\"PolicyDecisionEvent\",\"from_recommended_stage\":\"closure_candidate\",\"links_to\":\"AIE-E004\",\"reason_codes\":[\"source_contradiction\"],\"sort_order\":30,\"to_stage\":\"human_review\"},{\"case_id\":\"CASE-BG-CONTRA\",\"comment\":\"\",\"decision\":\"pending\",\"event_id\":\"HRE-CASE-BG-CONTRA-PENDING\",\"event_type\":\"HumanReviewEvent\",\"sort_order\":40,\"structured_task_output\":null,\"task_key\":null}],\"evidence_state\":{\"business_state\":\"green\",\"closure_block_reason\":\"source_contradiction\",\"derived_evidence_state\":\"contradicting\"},\"human_review_event\":{\"case_id\":\"CASE-BG-CONTRA\",\"comment\":\"\",\"decision\":\"pending\",\"event_id\":\"HRE-CASE-BG-CONTRA-PENDING\",\"event_type\":\"HumanReviewEvent\",\"structured_task_output\":null,\"task_key\":null},\"policy_decision_event\":{\"allowed_actions\":[\"human_review\",\"request_evidence\",\"open_investigation\"],\"block_reason\":\"source_contradiction\",\"case_id\":\"CASE-BG-CONTRA\",\"decision\":\"require_human_review\",\"decision_policy_version\":\"dp-v1\",\"event_id\":\"PDE-E-004\",\"event_type\":\"PolicyDecisionEvent\",\"from_recommended_stage\":\"closure_candidate\",\"links_to\":\"AIE-E004\",\"reason_codes\":[\"source_contradiction\"],\"to_stage\":\"human_review\"},\"policy_versions\":{\"decision_policy_version\":\"dp-v1\",\"interpretation_policy_version\":\"ip-v1\"},\"reviewer_packet\":{\"block_reason\":\"source_contradiction\",\"content\":\"Service recovery exception review required: CRM/order/billing/support notes are green, but fresh authoritative telemetry contradicts the business state. Do not close; open human exception review.\",\"evidence_table\":[{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"crm_order_status\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:00:00Z\",\"source\":\"crm\",\"ttl_seconds\":86400,\"value\":\"active\"},{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"billing_status\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:01:00Z\",\"source\":\"billing\",\"ttl_seconds\":86400,\"value\":\"clear\"},{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"inventory_assignment\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:02:00Z\",\"source\":\"inventory\",\"ttl_seconds\":86400,\"value\":\"assigned_match\"},{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"service_live_status\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:03:00Z\",\"source\":\"network_telemetry\",\"ttl_seconds\":300,\"value\":\"not_live\"},{\"authoritative\":true,\"case_id\":\"CASE-BG-CONTRA\",\"field\":\"dispatch_status\",\"freshness_status\":\"fresh\",\"observed_at\":\"2026-06-18T10:04:00Z\",\"source\":\"dispatch\",\"ttl_seconds\":86400,\"value\":\"complete\"}],\"policy_decision\":{\"allowed_actions\":[\"human_review\",\"request_evidence\",\"open_investigation\"],\"block_reason\":\"source_contradiction\",\"case_id\":\"CASE-BG-CONTRA\",\"decision\":\"require_human_review\",\"decision_policy_version\":\"dp-v1\",\"event_id\":\"PDE-E-004\",\"event_type\":\"PolicyDecisionEvent\",\"from_recommended_stage\":\"closure_candidate\",\"links_to\":\"AIE-E004\",\"reason_codes\":[\"source_contradiction\"],\"to_stage\":\"human_review\"},\"raw_agent_recommendation\":{\"adversarial_interpretation\":null,\"case_id\":\"CASE-BG-CONTRA\",\"confidence\":0.82,\"customer_impact_summary\":null,\"event_id\":\"AIE-E004\",\"event_type\":\"AgentInterpretationEvent\",\"evidence_gaps\":[],\"failure_category\":\"activation_failure\",\"interpretation_policy_version\":\"ip-v1\",\"operator_note\":null,\"rationale\":\"Business systems look complete, so the agent recommends closure pending policy review.\",\"recommended_actions\":[],\"recommended_next_stage\":\"closure_candidate\",\"reviewer_questions\":[],\"urgency\":null},\"recommended_options\":[\"human_review\",\"request_evidence\",\"open_investigation\"],\"rendering_status\":\"structured_packet_ready\"},\"service_id\":\"SVC-BG-1\"}",
    "CreatedAt": "2026-06-26T10:06:49.285992+00:00",
    "UpdatedBy": "F5E77DBA-8B15-4103-8605-DC11685DD53E",
    "RecordOwner": "F5E77DBA-8B15-4103-8605-DC11685DD53E",
    "CreateTime": "2026-06-26T10:07:15.6602766+00:00",
    "CreatedBy": "F5E77DBA-8B15-4103-8605-DC11685DD53E",
    "UpdateTime": "2026-06-26T10:07:15.6602766+00:00",
    "Id": "F9D838CE-4671-F111-AC9A-0022489A9A06"
  }
}

(exit 0)
```

## `uip df records query 35e8f6c7-4671-f111-ac9a-002248a16d28 --body {"selectedFields":["Id","CaseId","ScenarioId","ServiceId","BusinessState","DerivedEvidenceState","ClosureBlockReason","InterpretationPolicyVersion","DecisionPolicyVersion","SourceCaseInstanceKey","SourceTaskId","PackageVersion"],"filterGroup":{"logicalOperator":0,"queryFilters":[{"fieldName":"CaseId","operator":"=","value":"CASE-BG-CONTRA"}]}} --limit 5 --output json`

```text
{
  "Result": "Success",
  "Code": "RecordQuery",
  "Data": {
    "Items": [
      {
        "Id": "F9D838CE-4671-F111-AC9A-0022489A9A06",
        "CaseId": "CASE-BG-CONTRA",
        "ScenarioId": "E-004",
        "ServiceId": "SVC-BG-1",
        "BusinessState": "green",
        "DerivedEvidenceState": "contradicting",
        "ClosureBlockReason": "source_contradiction",
        "InterpretationPolicyVersion": "ip-v1",
        "DecisionPolicyVersion": "dp-v1",
        "SourceCaseInstanceKey": "9fc6fece-55ed-4fb2-b11a-6c96f7a3314e",
        "SourceTaskId": "4328396",
        "PackageVersion": "1.0.6"
      }
    ],
    "TotalCount": 1,
    "HasNextPage": false,
    "CurrentPage": 1,
    "TotalPages": 1,
    "SupportsPageJump": true
  }
}

(exit 0)
```

## `uip df records query 35e8f6c7-4671-f111-ac9a-002248a16d28 --body {"selectedFields":["Id","case_id","CaseId"],"filterGroup":{"logicalOperator":0,"queryFilters":[{"fieldName":"case_id","operator":"=","value":"CASE-BG-CONTRA"}]}} --limit 5 --output json`

```text
{
  "Result": "Failure",
  "Message": "Error querying records",
  "Instructions": "Query entity data failed. Filter field case_id does not exist or is deleted in entity ServiceRecoveryAuditBundleV2/35e8f6c7-4671-f111-ac9a-002248a16d28."
}

(exit 1)
```
