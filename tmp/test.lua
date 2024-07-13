local MOD = DECLARE_MODULE("role_funcs.annotations_list")

DECLARE_RUNNING_ATTR(MOD, "__attr_dict", {})


---@alias userId integer Then Id of a user

---@alias mode "r" | "w"

---@alias op_type
---| '1' # update type
---| '2' # add type
---| '3' # delete type

---@alias Handler fun(type: string, data: any):nil



function MOD.start()
    local a, b = nil, nil
    MOD:call_agent(1, 1)
    MOD:addHandler()
    MOD.doSomething()
    MOD.doSomething(a --[[@as string]], b)
    MOD:http_get()
    MOD.outdated()

    ---@type integer|nil|table|boolean
    local x

    -- @as
    -- @cast
    -- @class
    MOD.ff()
end

---comment
---@param uuid userId
---@param mode mode
---@param type op_type
function MOD:call_agent(uuid, mode, type)
end

---@param handler Handler
function MOD:addHandler(handler)
end

---@param key string muset bu string
---@param value integer muset bu integer
---@param value2 number muset bu float
---@param value3 boolean muset
function MOD:doSomething(key, value, value2, value3)
end

---@async
---Perform an asynchronous HTTP GET request
function MOD:http_get(url)
end

---@deprecated
function MOD:outdated() 
    
end
