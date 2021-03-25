import React from "react"

const Search=()=>{


    return(
       
        <div className="card search-card">
             
            <input type="text" placeholder="king" name="king"/>
            <input type="text" placeholder="location" name="location"/>
            <input type="text" placeholder="type" name="type"/>
            <button className="btn waves-effect waves-light #1976d2 blue darken-2"
             >search
            </button>
        </div>
    )
}
export default Search;