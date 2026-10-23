from fastmcp import FastMCP
import random
import json

mcp=FastMCP("Simple Calculator")

@mcp.tool
def cal_per(a:int,b:int)->int:
    """
        find a percentage of b.
        Args:
        a: first number
        b: second number
        return percentage as a*b/100

    """
    return a*b/100

@mcp.tool
def cal_ratio(a:int,b:int)->int:
    """Calculate ratio of a and b 
       Args:
           a:first number
           b:second number
           return a/b
    """
    return a/b

@mcp.resource("info://server")
def server_info()->str:
    """Get information about this server."""
    info={
        "name":"Simple calculator",
        "version":"1.0.0",
        "description":"A basic MCP server with math tools",
        "tools":["cal_per","cal_ratio"],
        "author":"Farhan"
    }
    return json.dumps(info,indent=2)

# start server
if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)