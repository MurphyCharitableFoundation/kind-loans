import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';



function ToggleButtonGroupForBusinesses(props){
    return(
    <ToggleButtonGroup value={props.business} onChange={props.handleBusiness} sx={{ flexWrap: "wrap"}}>
        {props.FilterButtonBusinesses.map((business,i) => {
            return <ToggleButton 
                    key={business.id} 
                    value={business.text}
                    sx={{ margin: 2,"&.Mui-selected, &.Mui-selected:hover": {backgroundColor: '#07001C!important'}}}
                    style={{borderRadius: '12px', color:'#FFFFFF',backgroundColor: '#A3A3A3'}}
                    >
                {business.text}
            </ToggleButton>})}
    </ToggleButtonGroup>
    )
}



export default ToggleButtonGroupForBusinesses
