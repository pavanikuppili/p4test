//# This is a p4 code.
/*******************************************************************************
 *  INTEL CONFIDENTIAL
 *
 *  Copyright (c) 2021 Intel Corporation
 *  All Rights Reserved.
 *
 *  This software and the related documents are Intel copyrighted materials,
 *  and your use of them is governed by the express license under which they
 *  were provided to you ("License"). Unless the License provides otherwise,
 *  you may not use, modify, copy, publish, distribute, disclose or transmit
 *  this software or the related documents without Intel's prior written
 *  permission.
 *
 *  This software and the related documents are provided as is, with no express
 *  or implied warranties, other than those that are expressly stated in the
 *  License.
 ******************************************************************************/

#include <core.p4>
#include <v1model.p4>
//#endif

// #include "common/headers.p4"
// #include "common/util.p4"


struct metadata_t {}
struct header_t {}
//PortId_t NODE2_PORT;
// ---------------------------------------------------------------------------
// Ingress parser
// ---------------------------------------------------------------------------

parser MyIngressParser(packet_in pkt, out header_t hdr,
         inout metadata_t md, inout standard_metadata_t st_md) {
    state start {
        transition accept;
    }
}


control Checksum(inout header_t hdr, inout metadata_t md) { apply {} }

control Checksum2(inout header_t hdr, inout metadata_t md) { apply {} }

control SwitchIngress(inout header_t hdr, inout metadata_t md, inout standard_metadata_t st_md) {
    apply {
        if(st_md.ingress_port==160) {
            st_md.egress_port=132;
        } else if(st_md.ingress_port==132) {
            st_md.egress_port=160;
        }
    }
}


control SwitchEgress(inout header_t hdr, inout metadata_t md, inout standard_metadata_t st_md) {
    apply { }
}

control deparser(packet_out pkt, in header_t hdr) {
    apply{ }
}


V1Switch(MyIngressParser(), Checksum(), SwitchIngress(), SwitchEgress(), Checksum2(), deparser()) main;
