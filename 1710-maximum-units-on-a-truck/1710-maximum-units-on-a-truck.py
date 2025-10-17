class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #each boxType will have [no_of_boxes, units_per_box]
        #we need to fill the boxes with most units_per_box

        boxTypes.sort(key= lambda boxes: -boxes[1])
        boxes = 0
        units = 0
        i=0

        while i<len(boxTypes) and boxes<=truckSize:

            [num_boxes, num_units] = boxTypes[i]

            if boxes+num_boxes <= truckSize:
                boxes+=num_boxes

            else:
                num_boxes = truckSize - boxes
                boxes = truckSize
                
            i+=1
            units += (num_boxes * num_units)

        return units


            
            
            