import React, { useEffect, useState ,useContext} from 'react';
const Home=()=>{
const [dataa,setData]=useState([])

    useEffect(()=>{
        fetch("/stats",{method: 'get'}).then(Response=>Response.json() 
        .then(data=>{
            setData(data)
        }))
     },[])
const data=JSON.stringify(dataa, null, 1)
console.log(typeof(data));
return (
    
    <div>
        <pre>{data}</pre>
    </div>
)
}
export default Home;