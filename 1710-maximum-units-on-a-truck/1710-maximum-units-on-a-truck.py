class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #each boxType will have [no_of_boxes, units_per_box]
        #we need to fill the boxes with most units_per_box

        boxTypes.sort(key= lambda boxes: -boxes[1])
        units = 0

        for boxes,uni in boxTypes:
            
            boxes = min(boxes, truckSize)
            units+= uni * boxes
            truckSize -= boxes
            if truckSize == 0:
                break
        
        return units


            
            
            