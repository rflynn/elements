use <text_on/text_on.scad>;

difference()
{
	cube([50,50,3]);
	translate([3,3,2.7])
	{
		cube([44,44,0.3]);
	}
}

translate([40,41.5,2.7])
{
    text_extrude("12",extrusion_height=0.3,size=7,font="Trebuchet MS");
}

translate([25,26,2.7])
{
    text_extrude("Mg",extrusion_height=0.3,size=14.5,font="CenturySchoolbookT.");
}

translate([25,12,2.7])
{
    text_extrude("Magnesium",extrusion_height=0.3,size=5.5,font="Arial");
}

translate([25,6,2.7])
{
    text_extrude("24.305",extrusion_height=0.3,size=4,font="Trebuchet MS");
}
